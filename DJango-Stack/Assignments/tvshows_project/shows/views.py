from django.shortcuts import render, redirect, get_object_or_404
from .models import TVShow

# Create your views here.

# Display all shows
def index(request):
    shows = TVShow.objects.all()
    return render(request, 'shows/index.html', {'shows': shows})

# Form for new show
def new(request):
    return render(request, 'shows/new.html')

# Create a new show
def create(request):
    if request.method == 'POST':
        TVShow.objects.create(
            title=request.POST['title'],
            network=request.POST['network'],
            release_date=request.POST['release_date'],
            description=request.POST['description']
        )
        return redirect('shows:index')

# Display a single show
def show(request, id):
    show = get_object_or_404(TVShow, pk=id)
    return render(request, 'shows/show.html', {'show': show})

# Form to edit a show
def edit(request, id):
    show = get_object_or_404(TVShow, pk=id)
    return render(request, 'shows/edit.html', {'show': show})

# Update a show
def update(request, id):
    show = get_object_or_404(TVShow, pk=id)
    if request.method == 'POST':
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release_date']
        show.description = request.POST['description']
        show.save()
        return redirect('shows:show', id=show.id)

# Delete a show
def destroy(request, id):
    show = get_object_or_404(TVShow, pk=id)
    show.delete()
    return redirect('shows:index')