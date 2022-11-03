from django.urls import path  # import path function

from . import views  # same directory

urlpatterns = [
    path('', views.index, name='index'),  # route, view, 별칭 붙이기
    path('total', views.total, name='total'),
    path('kangwon', views.show_kangwon, name='kangwon'),
    path('get_counties_ajax/', views.get_counties_ajax, name="get_counties_ajax"),
]