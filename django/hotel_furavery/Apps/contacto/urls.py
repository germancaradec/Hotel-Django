from django.urls import path
from .views import ConsultaView

urlpatterns = [
    path('consultas/', ConsultaView.as_view(), name='consulta_list'),
    path('consultas/<int:id>', ConsultaView.as_view(), name='consulta_process'),
]