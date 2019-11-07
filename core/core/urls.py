
from django.contrib import admin
from django.urls import path,include
from clientes.routes import urlpatterns as clientes_urls
from produtos.routes import urlpatterns as produtos_urls

api_uls = [
    path('clientes/', include(clientes_urls)),
    path('produtos/', include(produtos_urls)),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(api_uls))


]
