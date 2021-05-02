from django.conf.urls import url, include
from ..contact_app import views

urlpatterns = [
    url(r'^$', views.ContactView.as_view()),
]
