from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import HashKey
from users.decorators import jwt_authentication_required
from django.views.decorators.http import require_http_methods
import requests, json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])
def protected_view(request):
    data = {
            "status": "success",
            "status_code": 200
        }
    return Response(data) 


class ETFListAPIView(ListAPIView):
    
    queryset = HashKey.objects.all()

    @jwt_authentication_required
    def list(request, *args, **kwargs):
        # import pdb; pdb.set_trace()
        res = requests.get('https://financialmodelingprep.com/api/v3/etf/list?apikey=ff170cfbc214454f0a10844eb6e9606e')
        # json_data = json.dumps(res)
        data = {
            "status": "success",
            "status_code": 200,
            "result": res.json()
        }
        return Response(data)

