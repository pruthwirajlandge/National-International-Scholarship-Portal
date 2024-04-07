from django.contrib import admin
from django.urls import path,include,re_path
from authentication.initials import create_default_profile
from django.conf import settings
from django.conf.urls.static import static
from django.db.models.signals import post_migrate
from authentication.views import Me, create_profile
from model.views import SchemeViewSet
from rest_framework.routers import DefaultRouter
from djoser import views

router = DefaultRouter()
router.register(r'scheme', SchemeViewSet,basename="scheme")

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('create-profile/', create_profile),
    path('my-account/', Me.as_view()),
    path('', include(router.urls)),
    path(r"login/", views.TokenCreateView.as_view(), name="login"),
    path('verification/', include('verify_email.urls')),
]

if settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

post_migrate.connect(create_default_profile)