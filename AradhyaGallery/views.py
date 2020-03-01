from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Gallery,GalleryForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.
def gallery_view(request):
    data = Gallery.objects.all()
    return render(request,'gallery/gallery_view.html',{'data':data})
@method_decorator(login_required(login_url='/authentication/'),name='dispatch')
class Create_Gallery(CreateView):
    form_class = GalleryForm
    template_name = 'gallery/create_gallery.html'
    success_url = '/gallery_view'

@method_decorator(login_required(login_url='/authentication/'),name='dispatch')
class Update_Gallery(UpdateView):
    form_class = GalleryForm
    template_name = 'gallery/create_gallery.html'
    success_url = '/gallery_view'
    def get_queryset(self):
        id = self.kwargs['pk']
        return Gallery.objects.filter(pk=id)
        
@method_decorator(login_required(login_url='/authentication/'),name='dispatch')
class Delete_Gallery(DeleteView):
    model = Gallery
    success_url = '/gallery_view/'
    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)