from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from menuApp.views import index, menu_list,menu_details, menu_delete


urlpatterns = [
    path('', index, name='index'),
    path('menus/', menu_list, name='menu_list'),
    path('menus/<int:pk>/', menu_details, name='menu_details'),
    path('menus/<int:pk>/delete/',menu_delete, name='menu_delete')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
