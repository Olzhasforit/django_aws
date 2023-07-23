from django.shortcuts import render
from .forms import AwsForm
from django.http import HttpResponseRedirect
from .models import Bucket

def aws(request):
    submitted=False
    buckets=Bucket.objects.all()
    if request.method == 'POST':
        form=AwsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/aws?submitted=True')
    else:
        form=AwsForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'aws/aws.html', {'form':form, 'submitted':submitted, 'buckets':buckets})


# Create your views here.
