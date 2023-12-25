"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import index, pagina_404
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

'''
handler404 = pagina_404 se utiliza para personalizar el manejo de errores 404 en tu aplicación Django, utilizando la función pagina_404.
'''
handler404 = pagina_404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('', include('apps.posts.urls')),
    path('', include('apps.contacto.urls')),
    path('', include('apps.usuario.urls')),
    path('', include('django.contrib.auth.urls')),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)# Define dos patrones de url para servir archivos estaticos y multimedia

# Estas líneas configuran Django para servir archivos estáticos y multimedia 
# en URL específicas según su configuración.
# Esto permite que su aplicación acceda y entregue estos archivos al navegador 
# para la correcta representación de sus páginas web.
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# *Solo se utiliza en desarrollo*