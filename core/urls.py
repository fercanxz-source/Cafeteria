from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name="index"),
    path('about/', TemplateView.as_view(template_name="about.html"), name="about"),
    path('store/', TemplateView.as_view(template_name="store.html"), name="store"),
    path('contact/', TemplateView.as_view(template_name="contact.html"), name="contact"),
    path('sample/', TemplateView.as_view(template_name="sample.html"), name="sample"),
]