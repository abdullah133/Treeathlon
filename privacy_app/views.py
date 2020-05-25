from django.shortcuts import render
from .models import Privacy
# Create your views here.
def privacyview(request):
    privacy_description = Privacy.objects.all()
    context = {'privacy_description':privacy_description,

                }
    return render(request, 'privacy_app/privacy.html', context = context)
