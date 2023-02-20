from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.urls import path

urlpatterns = [
    path('login/',views.LoginPage,name="LoginPage"),
    path('regester/',views.RegesterPage,name="RegesterPage"),
    path('password/',views.PasswordPage,name="PasswordPage"),
    path('forgot_otp/',views.forgot_otp,name="forgot_otp"),
    path('forgot_password/',views.forgot_pass,name="forgot_pass"),
    path('new_pass/',views.new_pass,name="new_pass"),
] 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATICFILES_DIRS)
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)