from django.urls import path
from . import views

urlpatterns = [
    # Gallery View
    path('',views.gallery_view,name='gallery_view'),
    path('create_gallery/',views.Create_Gallery.as_view(),name='create_gallery'),
    path('update_gallery/<int:pk>/',views.Update_Gallery.as_view(),name='update_gallery'),
    path('delete_gallery/<int:pk>/',views.Delete_Gallery.as_view(),name='delete_gallery'),


]