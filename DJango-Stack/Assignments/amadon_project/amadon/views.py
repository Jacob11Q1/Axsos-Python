from decimal import Decimal
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.db.models import Sum
from .models import Product, Order

# Create your views here.

def product_list(request):
    """
    Show all products with a small form per product. The form sends only:
      - product_id (hidden)
      - quantity (select)
    No price field is included in the form.
    """
    products = Product.objects.all()
    return render(request, 'amadon/product_list.html', {'products': products})


@require_POST # Enforces POST only on buy endpoint
def buy(request):
    """
    Handle POST only. This view:
      1) reads product_id and quantity
      2) looks up the product + price server-side
      3) creates an Order (server calculates total)
      4) redirects to the checkout page (PRG pattern)
    IMPORTANT: do NOT render a template on POST.
    """
    product_id = request.POST.get('product_id')
    quantity_raw = request.POST.get('quantity', '1')

    # convert and validate quantity server-side
    try:
        quantity = int(quantity_raw)
        if quantity < 1:
            quantity = 1
    except ValueError:
        quantity = 1

    product = get_object_or_404(Product, pk=product_id)

    # price taken from DB — never use client provided price
    unit_price = product.price

    # create order; Order.save will compute total_price
    order = Order.objects.create(
        product=product,
        quantity=quantity,
        price_at_purchase=unit_price
    )

    # Redirect to checkout page -> PREVENTS duplicate orders on refresh (PRG)
    return redirect('amadon:checkout')


def checkout(request):
    """
    GET-only page that shows the most recent order and aggregated stats:
        - total quantity of all orders
        - total amount charged (sum of total_price for all orders)
    Refreshing this page will NOT re-process any POST.
    """
    last_order = Order.objects.order_by('-created_at').first()

    agg = Order.objects.aggregate(
        total_quantity=Sum('quantity'),
        total_amount=Sum('total_price')
    )

    total_quantity = agg['total_quantity'] or 0
    total_amount = agg['total_amount'] or Decimal('0.00')

    context = {
        'last_order': last_order,
        'total_quantity': total_quantity,
        'total_amount': total_amount,
    }
    return render(request, 'amadon/checkout.html', context)