from django.contrib import admin

from django.urls import path, include

from gestion import views

from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('voluntarios/', views.voluntario_list, name='voluntario_list'),
    path('eventos/', views.evento_list, name='evento_list'),
    path('', include('gestion.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
