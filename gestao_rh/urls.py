
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path
from rest_framework import routers
from apps.core import views
from apps.funcionarios.api.views import FuncionarioViewSet
from apps.registro_horas_extra.api.views import RegistroHorasExtraViewSet

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'api/funcionarios', FuncionarioViewSet)
router.register(r'api/registro_hora_extra', RegistroHorasExtraViewSet)

urlpatterns = [
    path('', include('apps.core.urls')),
    path('funcionarios/', include('apps.funcionarios.urls')),
    path('departamentos/', include('apps.departamentos.urls')),
    path('empresa/', include('apps.empresa.urls')),
    path('documentos/', include('apps.documentos.urls')),
    path('horas-extras/', include('apps.registro_horas_extra.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
