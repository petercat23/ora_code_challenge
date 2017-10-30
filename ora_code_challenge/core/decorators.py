from django.conf import settings

from rest_framework_simplejwt.serializers import TokenRefreshSerializer


def rotate_JWT(func):
    """
    Assumes the user is authenticated. Probably a way to work that in with Django's
    @login_required decorator.

    Not sure if it would be best to include refresh old refresh token along with old access
    token if refresh isn't included in request.
    """
    def decorated_function(self, request, *args, **kwargs):
        self.headers = {'Authorization': request.META['HTTP_AUTHORIZATION']}
        if 'headers' in request.META and 'refresh' in request.META['headers']:
            raw_token = request.META['headers']['refresh'].split(" ")[-1]

            token_serializer = TokenRefreshSerializer(data={'refresh': raw_token})
            token_serializer.is_valid(raise_exception=True)
            access = token_serializer.validated_data['access']
            refresh = token_serializer.validated_data['refresh']

            self.headers['Refresh'] = settings.JWT_HEADER_TYPE + refresh
            self.headers['Authorization'] = settings.JWT_HEADER_TYPE + access

        return func(self, request, *args, **kwargs)
    return decorated_function
