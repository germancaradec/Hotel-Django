from django.views import View
from .models import Consulta
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
class ConsultaView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            consultas = list(Consulta.objects.filter(id=id).values())
            if len(consultas) > 0 :
                consulta = consultas[0]
                datos = {'message': "Consulta obtenida correctamente", 'consulta': consulta}
            else:
                datos = {'message': "Consultas no encontradas..."}
            return JsonResponse(datos)
        else:
            consultas = list(Consulta.objects.values())
            if len(consultas) > 0:
                datos = {'message': "Consultas obtenidas correctamente", 'consultas': consultas}
            else:
                datos = {'message': "Consultas no encontradas..."}
            return JsonResponse(datos)

    def post(self, request):
        print(request.body)
        jd = json.loads(request.body)
        print(jd)
        Consulta.objects.create(nombre=jd['nombre'], apellido=jd['apellido'], telefono=jd['telefono'], texto=jd['texto'])
        datos = {'message': "Consulta agregada correctamente"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        consultas = list(Consulta.objects.filter(id=id).values())
        if len(consultas) > 0 :
            consulta = Consulta.objects.get(id=id)
            consulta.nombre = jd['nombre']
            consulta.apellido = jd['apellido']
            consulta.telefono = jd['telefono']
            consulta.texto = jd['texto']
            consulta.save()
            datos = {'message': "Consulta modificada correctamente"}
        else:
            datos = {'message': "Consultas no encontradas..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        consultas = list(Consulta.objects.filter(id=id).values())
        if len(consultas) > 0 :
            Consulta.objects.filter(id=id).delete()
            datos = {'message': "Consulta eliminada correctamente"}
        else:
            datos = {'message': "Consultas no encontradas..."}
        return JsonResponse(datos)