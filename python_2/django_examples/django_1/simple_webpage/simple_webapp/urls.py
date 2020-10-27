from django.conf.urls import url
from simple_webapp import views

urlpatterns=[
    url("^$", views.Home.as_view() ),
    url("^generic/$", views.Generic.as_view() ),
    url("^elements/$", views.Elements.as_view() )
]