
from django.urls import path,include
from . import views

urlpatterns = [
  path('textdata',views.testfunction,name='textdata'),
  path('call',views.testfunction,name='call'),
  path('text',views.testfunction,name='text'),
  path('text1',views.testfunction,name='text1')
]