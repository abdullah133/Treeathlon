from django.shortcuts import render
from .models import Team, TeamDescription
# Create your views here.
def aboutview(request):
    teambilder = Team.objects.all()
    team_description = TeamDescription.objects.all()
    mein_header_bild = 'contact-banner-area relative'
    context = {'teambilder':teambilder,
                'team_description':team_description,
                'mein_header_bild':mein_header_bild,
                }
    return render(request, 'about_app/about.html', context = context)
