from django.shortcuts import render
from django.http import HttpResponse
from Database.utils import details

# Create your views here.


def index(request):  # request -> HTTP request object
    return HttpResponse("안녕하세요 우리동네변호사에 오신것을 환영합니다.")


def total(request):  # 전체 표를 보여줍니다.
    return HttpResponse(str(details))

def showManger(request):
    total_list = details

