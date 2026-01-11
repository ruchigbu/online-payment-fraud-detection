from . import views
from django.urls import path


urlpatterns=[
    path("",views.home, name="home"),
    path("detect_fraud/",views.detect_fraud, name="detect fraud"),
    
]