from django.urls import path

from . import views

urlpatterns = [
    path('', views.VoyageList.as_view()),
    path('dataframes',views.VoyageDataFrames.as_view()),
    path('cache',views.VoyageDataFrames2.as_view()),
    path('geo',views.VoyagePlaceList.as_view()),
    path('aggregations',views.VoyageAggregations.as_view()),
	path('autocomplete',views.VoyageTextFieldAutoComplete.as_view())
    ]