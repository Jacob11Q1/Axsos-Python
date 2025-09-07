from django.shortcuts import render, redirect, get_object_or_404
from .models import TVShow
from .forms import TVShowForm

# Create your views here.

# Display all shows
def shows_list(request):
    shows = TVShow.objects.all().order_by('-created_at')
    return render(request, 'shows/shows_list.html', {'shows': shows})

# Add a new show
def add_show(request):
    if request.method == "POST":
        form = TVShowForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shows:shows_list')
    else:
        form = TVShowForm()
    return render(request, 'shows/add_show.html', {'form': form})

# Edit existing show
def edit_show(request, show_id):
    show = get_object_or_404(TVShow, id=show_id)
    if request.method == "POST":
        # allow updating current show without raising uniqueness error
        form = TVShowForm(request.POST, instance=show)
        if form.is_valid():
            form.save()
            return redirect('shows:shows_list')
    else:
        form = TVShowForm(instance=show)
    return render(request, 'shows/edit_show.html', {'form': form, 'show': show})

# Delete show
def delete_show(request, show_id):
    show = get_object_or_404(TVShow, id=show_id)
    show.delete()
    return redirect('shows:shows_list')

def show(request, show_id):
    show = get_object_or_404(TVShow, id=show_id)
    return render(request, 'shows/show.html', {'show': show})