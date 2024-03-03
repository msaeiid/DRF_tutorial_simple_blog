from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


def create_jwt_pair_for_user(user: User):
    """
    Sometimes, you may wish to manually create a token for a user. This could be done as follows:
    :param user:
    :return:
    """
    refresh = RefreshToken.for_user(user)
    token = {
        "access": str(refresh.access_token),
        "refresh": str(refresh)
    }
    return token
