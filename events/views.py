from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Projects
from .forms import NewProjForm
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.


@login_required(login_url="login_page")
def projects(response):
    try:
        data = Projects.objects.all()
        context = {
            'proj' : data
        }
    except :
        context = {
            'proj' : 'Data not Found'
        }
    return render(response, 'events_crud/eventsLand.html', context)



def NewProject(response):
    form = NewProjForm(response.POST)

    if response.method == 'POST':
    
        if form.is_valid():
            form.save()
            messages.success(response, "Project Added Successfully")
            # yahan pe success is the message.info

            return redirect('proj')

    context = {"form" : form}
    return render(response, 'events_crud/eventsNew.html', context)

def DelProject(response, id):
    data = Projects.objects.get(id=id)
    data.delete()

    return redirect('proj')

def UpProject(response, id):
    data = Projects.objects.get(id=id)
    Upform = NewProjForm(response.POST or None, instance=data)
    
    if Upform.is_valid():
        Upform.save()
        messages.success(response, "Project Updated Successfully")

        return redirect('proj')

    context = {"form" : Upform}
    return render(response, 'ProjectUpdate.html', context)


def events_signup(request):
    return render(request, 'events_signup.html')