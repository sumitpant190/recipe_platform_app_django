from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from recipes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Includes all auth-related URLs
    path('accounts/signup/', views.signup, name='signup'),
    path('recipes/', include('recipes.urls')),
    path('', views.recipe_list, name='recipe_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
