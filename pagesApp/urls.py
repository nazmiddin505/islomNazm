from django.urls import path
from .views import mainPageView, aboutPageView, siyamPageView

urlpatterns = [
    path('', mainPageView.as_view(), name = 'main'),
    path('about', aboutPageView.as_view(), name = 'about'),
    path('siyam',siyamPageView.as_view(), name = 'siyam')
]