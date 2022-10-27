from django.shortcuts import render
from django.http import HttpResponse
from Database.utils import details
from collections import deque
from django.shortcuts import render


# Create your views here.


def index(request):  # request -> HTTP request object, 첫 페이지
    return render(request, 'home/index.html', {
                      'form': 'hi'
                  },
                  )


def total(request):  # 전체 표를 보여줍니다.
    return HttpResponse(str(details))


def show_kangwon(request):  # 강원도 목록 조회 코
    # kangwon = deque()
    # for detail in details:
    #     if detail['city'] == '강원':
    #         kangwon.append(detail)
    # return kangwon
    return render(request, 'home/index.html', {
                      'form': 'hi'
                  },
                  )
