from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class UserCreationForm(UserCreationForm):
    """
    If you want to add something in future
    """

    class Meta:
        model = User
        fields = ("phone_number",)


class UserChangeForm(UserChangeForm):
    """
    If you want to add something in future
    """

    class Meta:
        model = User
        fields = ("phone_number",)
