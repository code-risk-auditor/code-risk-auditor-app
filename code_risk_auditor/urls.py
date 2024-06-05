from django.urls import path

from code_risk_auditor import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('installed/callback', views.InstalledAppCallbackView.as_view(), name='installed_callback'),
]