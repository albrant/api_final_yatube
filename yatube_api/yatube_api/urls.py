from django.views.generic import TemplateView
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls', namespace='api')),
    path(
        'redocold/',
        TemplateView.as_view(template_name='api/redoc.html'),
        name='redocold'
    ),
]

schema_view = get_schema_view(
    openapi.Info(
        title="Posts API", default_version='v1',
        description="Документация для приложения Posts проекта Yatube_api",
        contact=openapi.Contact(email="skizee@yandex.ru"),
        license=openapi.License(name="BSD License")),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

urlpatterns += [
    url(r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'),
]
