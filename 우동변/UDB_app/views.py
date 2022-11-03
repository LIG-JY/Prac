from django.http import HttpResponse , JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from Database.lawyer_dao import ca_collection
from collections import deque

# Create your views here.
details = deque(ca_collection.find({}))  # CRUD 중 R, Cursor객체(pymongo에서 지원)를 list로 바꿨습니다.

document_ = ca_collection.find_one()  # colleciton에서 한 document를 찾습니다.
field_names = list(document_.keys())  # dictionray 내장 메소드로, key를 뽑아서, 리스트로 변환했습니다.

city_names = field_names[1]  # "city" , "county" , "emd"
city_list = ca_collection.distinct(city_names)

city_county_mapping = dict()  # 시/도 -> 시/군/구 mapping
for i, city in enumerate(city_list):
    city_query = {'city': f'{city}'}
    temp_cities = ca_collection.find(city_query)
    city_county_mapping[city] = temp_cities.distinct(field_names[2])  # field_names[2] == "county", key & value mapping

county_list = ca_collection.distinct(field_names[2])
county_emd_mapping = dict()  # 시/군/군 -> 읍/면/동 Mapping
for i, county in enumerate(county_list):
    county_query = {'county': f'{county}'}
    temp_counties = ca_collection.find(county_query)
    county_emd_mapping[county] = temp_counties.distinct(field_names[3])


def index(request):  # request -> HTTP request object, 첫 페이지
    return render(request, 'home/index.html',
                  )


def total(request):  # 전체 표를 보여줍니다.
    return HttpResponse(details)


def show_county(city="강원"):
    """
    :param city
    :return: 해당 city에 mapped county_list
    """
    return city_county_mapping[city]


def show_kangwon(request):  # 강원도만 보여주게
    counties = show_county()
    return render(request,
                  'show/index.html',
                  {'city_list': city_list, 'county_list': counties},
                  )


@csrf_exempt
def get_counties_ajax(request):
    if request.method == "POST":
        county_id = request.POST['city_id']  # "강원"
        context = {'county_id': county_id}
        return JsonResponse(context)
        # return JsonResponse(safe=False)


