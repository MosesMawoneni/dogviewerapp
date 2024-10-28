from django.urls import path


from . import views
app_name = 'dogs'
urlpatterns = [
    path("",views.ShowAllDogsList.as_view(),name="dog-list"),
]