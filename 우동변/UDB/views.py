from django.shortcuts import render
from django.http import HttpResponse
from Database.utils import details

# Create your views here.


def index(request):  # request -> HTTP request object, 첫 페이지
    return HttpResponse("안녕하세요 우리동네변호사에 오신것을 환영합니다.")


def total(request):  # 전체 표를 보여줍니다.
    return HttpResponse(str(details))

def show(request):  # 목록 조회 코
    total_list = details

