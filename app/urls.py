from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from . forms import ForgotPasswordForm

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name="logout"),
    path('profile/<int:id>/', views.profilePage, name='profile'),
    path('update-profile/', views.updateProfile, name="update-profile"),
    path('forgot-password/', auth_view.PasswordResetView.as_view(template_name='app/forgot_password.html',
         form_class=ForgotPasswordForm), name='forgot-password'),

    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('category/<slug:val>', views.category, name='category'),
    path('category-title/<val>', views.categoryTitle, name='category-title'),
    path('product-detail/<int:pk>', views.productDetail, name='product-detail'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
