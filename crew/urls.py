from django.urls import path
from crew.views import IndexView

app_name = 'crew'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
