from django.urls import path
from . import views

urlpatterns = [
    # path('', views.liste_evenements, name = 'liste_evenements'),
    path('', views.index, name = 'index'),
    path('evenements/<int:event_id>/', views.detail_evenement, name='detail_evenement'),
]