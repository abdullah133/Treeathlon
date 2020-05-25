from .forms import JoinForm
from about_app.models import ContactInfo

def global_variables(request):
    form = JoinForm()
    info = ContactInfo.objects.all()
    context = {'join_form':form,
                'info':info,}
    return context
