from django.forms import ModelForm
from .models import UserInfo

class CamForm(ModelForm):

    class Meta:
        model = UserInfo
        fields = ("title","desc","pic")