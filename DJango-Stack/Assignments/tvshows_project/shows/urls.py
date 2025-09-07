from django.urls import path
from . import views

app_name = 'shows'

urlpatterns = [
    path('', views.index, name='index'),  # /shows
    path('new', views.new, name='new'),   # /shows/new
    path('create', views.create, name='create'),  # /shows/create
    path('<int:id>', views.show, name='show'),  # /shows/<id>
    path('<int:id>/edit', views.edit, name='edit'),  # /shows/<id>/edit
    path('<int:id>/update', views.update, name='update'),  # /shows/<id>/update
    path('<int:id>/destroy', views.destroy, name='destroy'),  # /shows/<id>/destroy
]