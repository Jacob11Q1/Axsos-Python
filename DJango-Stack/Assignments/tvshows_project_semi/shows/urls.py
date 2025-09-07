from django.urls import path
from . import views

app_name = 'shows' # To Define the namspace

urlpatterns = [
    path('', views.shows_list, name='shows_list'),
    path('add/', views.add_show, name='add_show'),
    path('<int:show_id>/', views.show, name='show'),
    path('edit/<int:show_id>/', views.edit_show, name='edit_show'),
    path('delete/<int:show_id>/', views.delete_show, name='delete_show'),
]
