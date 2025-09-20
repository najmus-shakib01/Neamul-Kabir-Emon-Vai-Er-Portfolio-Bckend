from django.urls import path
from .views import ContactFormView

# URL Patterns
urlpatterns = [
    path('contact/', ContactFormView.as_view(), name='contact-form'),
]