from django.urls import path

from source.views import check_status_view

urlpatterns = [
    path('check/', check_status_view, name='check_status')
]