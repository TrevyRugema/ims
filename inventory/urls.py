
from django.contrib import admin
from django.urls import path, include,re_path
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib.auth.models import User
# from rest_framework import routers,serializers,viewsets
from .views import dashboard


# # Serializers define the API representation
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model=User
#         fields=['url','username','email','is_staff']

# # ViewSets define the view behavior
# class UserViewSet(viewsets.ModelViewSet):
#     queryset=User.objects.all()
#     serializer_class=UserSerializer

# # Routers provide an easy way of automatically determining the URL conf.
# router=routers.DefaultRouter()
# router.register('users',UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('users/', include('users.urls')),
    path('aflink/', include('aflink.urls')),
    path('api/',include('api.urls')),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
   
]
urlpatterns += static(settings.MEDIA_URL, doument_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)