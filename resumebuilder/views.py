from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
from django.urls import reverse
from django.template.loader import render_to_string
from .models import Dest
#from .forms import NameForm
nd={"first":"ghgkhghghgkhg",
    "second":"vggfjhgjgkg",
    "third":"jhgyjgjygyg"}

# Create your views here.
def login(request):
    try:
        return render(request,"resumebuilder/input.html",{
            "text":nd["first"]
        })
    except:
        return HttpResponseNotFound("This is not working")

def index(request):
    try:
        dest1=Dest()
        
        dest1.fname=str(request.POST["fname"])
        dest1.lname=str(request.POST["lname"])
        
        return render(request,"resumebuilder/result.html",{
           'dest1':dest1
            
        })
    except:    
        return HttpResponseNotFound("This is not working")
