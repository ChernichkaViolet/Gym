from django.urls import path

from . import views
# from django.conf.urls import url

app_name="Gym"

urlpatterns = [
    path('list/', views.exercises_list, name='list'),
    path('create/', views.ExercisesCreate.as_view(), name='create'),
    path('update/<int:pk>', views.ExercisesUpdate.as_view(), name='update'),
    path('delete/<int:pk>', views.ExercisesDelete.as_view(), name='delete'),
    # path('detail/<int:pk>', views.ExercisesDetail.as_view(), name='detail'),
]
