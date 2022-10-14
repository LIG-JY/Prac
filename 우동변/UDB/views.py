from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request): # request -> HTTP request object
    return HttpResponse("안녕하세요 우리동네변호사에 오신것을 환영합니다.")

