from django.urls import path
from . import views

# domain.com/firstr_app/simple_view
urlpatterns = [
    path('', views.index, name='index'),
]