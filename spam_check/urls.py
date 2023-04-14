from django.urls import path
from . import views

urlpatterns = [
    path('',views.check_email, name='check_email'),
    path('output/',views.output,name='output'),
    path('details/',views.details,name='details')
]