from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomepageView.as_view(), name='home'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('paste/<int:pk>/', views.PasteDetailView.as_view(), name='paste_detail'),
    path('paste/<int:pk>/edit/',views.PasteUpdateView.as_view(), name='paste_edit'),
    path('paste/<int:pk>/delete/', views.PasteDeleteView.as_view(), name='paste_delete'),
]
