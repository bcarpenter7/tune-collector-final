from django.urls import path
from . import views




urlpatterns = [
path('', views.home, name='home'),
path('about/', views.about, name='about'),
path('tunes/', views.tunes_index, name='index'),
path('tunes/<int:tune_id>/', views.tunes_detail, name='detail'),
path('tunes/create/', views.TuneCreate.as_view(), name='tunes_create'),
path('tunes/<int:pk>/update', views.TuneUpdate.as_view(), name='tunes_update'),
path('tunes/<int:pk>/delete', views.TuneDelete.as_view(), name='tunes_delete'),
path('tunes/d', views.tunes_index_d, name='index_d'),
path('tunes/a', views.tunes_index_a, name='index_a'),
path('tunes/c', views.tunes_index_c, name='index_c'),
path('tunes/g', views.tunes_index_g, name='index_g'),
]
