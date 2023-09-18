from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead, Agent
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
  print()
  if request.method == "POST":
    print("Receiving a POST request")
    form = LeadForm(request.POST)
    if form.is_valid():
      print("The form is valid")
      print(form.cleaned_data)
      first_name = form.cleaned_data['first_name']
      last_name = form.cleaned_data['last_name']
      age = form.cleaned_data['age']
      agent = Agent.objects.first()
      print("The lead has been created")
  context = {
    "form":LeadForm()
  }
  return render(request, "leads/lead_create.html", context)