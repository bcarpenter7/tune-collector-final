from django.urls import path
from . import views

app_name = 'tune'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('tunes/', views.tunes_index, name='index'),
    path('tunes/<int:tune_id>/', views.tunes_detail, name='detail'),
    path('tunes/create/', views.TuneCreate.as_view(), name='create'),
    path('tunes/<int:pk>/update/', views.TuneUpdate.as_view(), name='update'),
    path('tunes/<int:pk>/delete/', views.TuneDelete.as_view(), name='delete'),
    path('tunes/<str:char>/', views.tunes_note_filter, name='note_filter'),
]
