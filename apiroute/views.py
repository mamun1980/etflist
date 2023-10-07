from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import ETL
from users.decorators import jwt_authentication_required
from django.views.decorators.http import require_http_methods

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])
@jwt_authentication_required
def protected_view(request):
    data = {
            "status": "success",
            "status_code": 200
        }
    return Response(data) 


class ETFListAPIView(ListAPIView):
    
    queryset = ETL.objects.all()

    def list(request, *args, **kwargs):
        data = {
            "status": "success",
            "status_code": 200
        }
        return Response(data)

