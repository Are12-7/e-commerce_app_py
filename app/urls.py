from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from . forms import PasswordResetForm, PasswordChangeForm,SetPasswordForm

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name="logout"),
    path('profile/<int:id>/', views.profilePage, name='profile'),
    path('update-profile/', views.updateProfile, name="update-profile"),
    
    # RESET PASSWORD
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='app/reset_password.html',
         form_class=PasswordResetForm), name='password_reset'),
    
    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(template_name='app/reset_password_done.html'), name='password_reset_done'),
    
    path('password-reset-confirm/<uidb64>/<token>', auth_view.PasswordResetConfirmView.as_view(template_name='app/reset_password_confirm.html',
         form_class=SetPasswordForm), name='password_reset_confirm'),
    
    path('reset-password-complete/', auth_view.PasswordResetCompleteView.as_view(template_name='app/reset_password_complete.html'), name='password_reset_complete'),
 
    #END RESET PASSWORD
    
    # CHANGE PASSWORD
    path('password-change/', auth_view.PasswordChangeView.as_view(template_name='app/password_change.html', form_class=PasswordChangeForm, success_url = '/password-change-complete'), name='password-change'),
    path('password-change-complete/', auth_view.PasswordChangeDoneView.as_view(template_name='app/password_change_complete.html'), name='change-password-done'),
    # END CHANGE PASSWORD
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('category/<slug:val>', views.category, name='category'),
    path('category-title/<val>', views.categoryTitle, name='category-title'),
    path('product-detail/<int:pk>', views.productDetail, name='product-detail'),
    # SHOPPING CART
    path('add-to-cart/', views.addToCart, name='add-to-cart'),
    path('cart/', views.showCart, name='cart'),
    path('plus-cart/', views.plusCart),
    path('minus-cart/', views.minusCart),
    path('remove-cart/', views.removeCart),
    #CHECKOUT
    path('checkout/', views.checkout_session, name='checkout'),
    path('cancel/', views.CancelPayment, name='cancel'),
    path('success/', views.SuccessfulPayment, name='success'),

    

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
