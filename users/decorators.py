# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import exceptions
from django.http import JsonResponse
from apiroute.models import HashKey


def jwt_authentication_required(view_func):
    """
    Custom decorator to authenticate JWT tokens.
    """
    def _wrapped_view(view, *args, **kwargs):
        request = view.request
        key = request.query_params.get('key')
        try:
            hash_key = HashKey.objects.get(hash=key)
            if hash_key:
                return view_func(request, *args, **kwargs)
            else:
                raise exceptions.AuthenticationFailed("JWT authentication failed")
        except exceptions.AuthenticationFailed as e:
            return JsonResponse({"error": str(e)}, status=401)

    return _wrapped_view
