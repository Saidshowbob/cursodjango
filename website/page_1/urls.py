from django.urls import path, include
from .views import main_page, save_form


urlpatterns = [
    path('', main_page),
    path('save-form/', save_form, name="save_form")
]
