from django.conf.urls import url

from webhook import views

urlpatterns = [
    url(r'^webhook/',views.webhook,name='webhook'),
]