from django.contrib.auth.models import User
from main.models import User
class NameAuthBackend:
    """
    Custom authentication backend.

    Allows users to log in using their first name.
    """

    def authenticate(self, request, email=None, name=None, password=None):
        """
        Overrides the authenticate method
        """
        try:
            if email == None:
                user = User.objects.get(name=name)
            else:
                user = User.objects.get(email=email)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """
        Overrides the get_user method
        """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None