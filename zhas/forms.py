from django.forms import ModelForm
from .models import Bucket

class AwsForm(ModelForm):
    class Meta:
        model = Bucket
        fields = '__all__'