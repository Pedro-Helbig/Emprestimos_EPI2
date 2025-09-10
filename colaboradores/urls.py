from django.urls import path
from . import views

app_name = "colaboradores"

urlpatterns = [
    path("", views.ColaboradorListView.as_view(), name="listar"),
    path("<int:pk>/", views.ColaboradorDetailView.as_view(), name="detalhar"),
    path("novo/", views.ColaboradorCreateView.as_view(), name="criar"),
    path("<int:pk>/editar/", views.ColaboradorUpdateView.as_view(), name="editar"),
    path("<int:pk>/excluir/", views.ColaboradorDeleteView.as_view(), name="excluir"),
]