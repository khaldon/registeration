from django.conf.urls import url
from . import views

app_name = 'log_sign_app'
urlpatterns = [
    url('sign_up/',views.get_sign_up,name='sign_up'),
    url('log_in/',views.log_in,name='log_in'),
]
