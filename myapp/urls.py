from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='home'),
    path('blog/<int:id>/',views.blog,name='blog'),
    path('edit/data/<int:id>/',views.edit_data,name='edit_data'),
    path('delete_data/<int:id>/',views.post_delete,name='delete_data'),
    path('about/',views.about,name='about'),
]
