from django.shortcuts import render, redirect
from polls.models import Project, Request
import smtplib
from django.http import HttpResponse
# Create your views here.
def index(request):
    if request.method == 'POST':
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login('dmakhambetali0806@gmail.com', 'ckqfszvescaqjpxz')
        name = str(request.POST.get('name'))
        email = str(request.POST.get('email'))
        message = str(request.POST.get('message'))
        
        message_org = f'{name}\n{email}\n{message}'
        # return HttpResponse(message_org)
        s.sendmail(from_addr='dmakhambetali0806@gmail.com',
                to_addrs='dmakhambetali0806@gmail.com',
                msg=message_org
                )
        s.quit()
        obj = Request.objects.create(name = name, email = email, message = message)
        obj.save()
        return redirect('/')
    projects = Project.objects.all().order_by('-date')
    return render(request, 'index.html', {'projects':projects})

