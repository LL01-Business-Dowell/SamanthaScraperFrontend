from django.shortcuts import render
from core.models import Notifications, ScraperFile
from django.http import HttpResponse
from rest_framework.views import APIView
from .serializers import NotificationsSerializer


# Create your views here.

class ScraperAlerts(APIView):
    serializer_class = NotificationsSerializer

    def post(self, request):
        data = request.POST.dict()
        serializer = self.serializer_class(data= data)

        if serializer.is_valid:
            serializer.save()

        return HttpResponse({"message": "success"}, status= 200)
    
class ScraperDownload(APIView):
    def post(self, request):
        #get data from scraper
        data = request.POST.dict()

        #retrieve matching file from unfinished queue and add download link to processed csv
        user_file = ScraperFile.objects.get(file_id= data['file_id'])
        user_file.download_link = data['download_link']
        user_file.save()

        #trigger alert notifying file owner to download their requested data
        alert = Notifications.objects.create(
            owner= user_file.owner,
            label = 'FILE READY',
            body = f'Your file of id: {user_file.id} has been processed and is now ready for download',
        )
        alert.save()

        return HttpResponse({"message": "success"}, status= 200)