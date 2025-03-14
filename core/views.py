from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import Notifications, ScraperFile
import requests
import secrets

# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')
    def post(self, request):
        if request.user.is_authenticated:
            #get file uploaded by user
            csv_file = request.FILES.get('postal_data')

            csv_data = {"csv_file": {csv_file.name, csv_file.file, "text/csv"}}
            
            #create and save log for new task in scraping queue
            user_file = ScraperFile.objects.create(
                owner= request.user,
                name= csv_file.name,
                file_id= secrets.token_hex(8)
            )
            user_file.save()
        

            data = {
                "document": user_file.id,
                "file_id": user_file.file_id,
                "owner": user_file.owner.id,
                "name": user_file.name,
            }

            #send file to scraper api
            scraper_api_url = '# SAMANTHA-SCRAPER-API-DOMAIN-NAME/process'
            scraper_task = requests.post(url= scraper_api_url, data= data, files= csv_data)

            #send notification


            #return to page with file log details


@login_required()
def processes_view(request):
    data = ScraperFile.objects.filter(owner= request.user)
    print(len(data))

    return render(request, 'processes.html', {"data": data})

@login_required()
def notification_view(request):
   
    try:
        notifications = request.user.notifications.all() 
        for alert in notifications:
            print(alert)
            if alert.viewed_status > 0:
                alert.viewed_status -= 1
                alert.save()
                print(alert.viewed_status)
    except:
        notifications = None

    return render(request, "notifications.html", {"notifications": notifications,})

def task_view(request, file_id):
    task = ScraperFile.objects.get(file_id= file_id)

    return render(request, "task.html", {"data": task})