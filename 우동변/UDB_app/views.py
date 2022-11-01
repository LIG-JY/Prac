from django.shortcuts import render
from django.http import HttpResponse
from Database.utils import details
from collections import deque
from django.shortcuts import render
from Database.utils import kangwon


# Create your views here.


def index(request):  # request -> HTTP request object, 첫 페이지
    return render(request, 'home/index.html',
                  )

def total(request):  # 전체 표를 보여줍니다.
    return HttpResponse(str(details))


def show_kangwon(request):  # 강원도만 보여주게
    return HttpResponse(kangwon)
