from django.urls import path, reverse_lazy
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='myauth'
urlpatterns = [
    path('signup/', views.SignUpPage, name='signup'),
    path('login/', views.LoginPage, name='login'),
    path('pswrdchange/', views.change_password, name='pswrdchange'),
    path('ajax/load-states/', views.load_states, name='ajax_load_states'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)





