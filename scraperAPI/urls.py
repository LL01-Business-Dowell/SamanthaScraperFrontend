from django.urls import path
from . import views

app_name = 'scraperAPI'

urlpatterns = [
    path('alerts/', views.ScraperAlerts.as_view(), name= 'scraper_alerts'),
    path('download/', views.ScraperDownload.as_view(), name= 'scraper_download'),
]