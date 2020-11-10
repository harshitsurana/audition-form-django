from django.urls import path, reverse_lazy
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='forms'
urlpatterns = [
    path('', views.FormListView.as_view()),
    path('forms/', views.FormListView.as_view(), name='all'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/update/', views.ProfileUpdateView.as_view(), name='profile_update'),
    path('form/<int:pk>', views.FormDetailView.as_view(), name='form_detail'),
    path('form/create',
        views.FormCreateView.as_view(success_url=reverse_lazy('forms:all')), name='form_create'),
    path('form/<int:pk>/update',
        views.FormUpdateView.as_view(success_url=reverse_lazy('forms:all')), name='form_update'),
    path('form/<int:pk>/delete',
        views.FormDeleteView.as_view(success_url=reverse_lazy('forms:all')), name='form_delete'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
        urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
