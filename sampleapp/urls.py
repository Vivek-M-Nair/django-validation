from django.urls import path
from . import views
urlpatterns=[
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('index/',views.index,name='index'),
    # path('register/',views.register_view,name='register_view'),
    # path('log/',views.log_view,name='log_view'),
    path('log_reg/',views.log_reg,name='log_reg')
]