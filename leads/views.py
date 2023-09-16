from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead
from .forms import LeadForm
# Create your views here.
def lead_list(request):
  # return HttpResponse("Hello World")
  # return render(request, "leads/home_page.html")
  leads = Lead.objects.all() 
  context = {
    "leads":leads
      }
  return render(request, "leads/lead_list.html", context)

def lead_detail(request, pk):
  print(pk)
  lead = Lead.objects.get(id=pk)
  context = {
    "lead":lead
  }
  return render(request,"leads/lead_detail.html", context)

def lead_create(request):
  context = {

  }
  return render(request, "leads/lead_create.html", context)