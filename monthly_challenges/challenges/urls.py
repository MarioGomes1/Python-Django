from django.urls import path

from . import views  # from same path import views


urlpatterns = [  # url config
    # if request reaches /january execute views.index
    path("", views.index, name="index"),
    path("<int:month>", views.monthly_challenges_by_number),
    path("<str:month>", views.monthly_challenges, name="month-challenge")
]
