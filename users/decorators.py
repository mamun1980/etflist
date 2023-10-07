# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import exceptions
from django.http import JsonResponse
from rest_framework_simplejwt.views import TokenVerifyView


def jwt_authentication_required(view_func):
    """
    Custom decorator to authenticate JWT tokens.
    """
    def _wrapped_view(request, *args, **kwargs):
        import pdb; pdb.set_trace()
        try:
            verify_view = TokenVerifyView.as_view()
            response = verify_view(request=request)
            if auth_tuple is not None:
                request.user, _ = auth_tuple
                return view_func(request, *args, **kwargs)
            else:
                raise exceptions.AuthenticationFailed("JWT authentication failed")
        except exceptions.AuthenticationFailed as e:
            return JsonResponse({"error": str(e)}, status=401)

    return _wrapped_view
