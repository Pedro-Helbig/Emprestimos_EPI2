# equipamentos/urls.py
from django.urls import path
from .views import (
    EquipamentoListView, EquipamentoDetailView,
    EquipamentoCreateView, EquipamentoUpdateView, EquipamentoDeleteView
)

urlpatterns = [
    path('equipamentos/', EquipamentoListView.as_view(), name='equipamentos_list'),
    path('equipamentos/create/', EquipamentoCreateView.as_view(), name='equipamentos_create'),
    path('equipamentos/<int:pk>/', EquipamentoDetailView.as_view(), name='equipamentos_detail'),
    path('equipamentos/<int:pk>/update/', EquipamentoUpdateView.as_view(), name='equipamentos_update'),
    path('equipamentos/<int:pk>/delete/', EquipamentoDeleteView.as_view(), name='equipamentos_delete'),
]
