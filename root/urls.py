from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from root.views import createUrl, routeToURL

urlpatterns = [
    path('', createUrl),
    path('<slug:key>',routeToURL)

]