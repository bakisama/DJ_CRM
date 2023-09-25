import random

from django.core.mail import send_mail
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from leads.models import Agent
from .forms import AgentModelForm


class AgentListView(LoginRequiredMixin, generic.ListView):
    template_name = "agents/agent_list.html"

    def get_queryset(self):
        return Agent.objects.all()


class AgentCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "agents/agent_create.html"
    form_class = AgentModelForm

    def get_success_url(self) -> str:
        return reverse("agents:agent-list")


class AgentDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "agents/agent_detail.html"


class AgentUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "agents/agent_update.html"


class AgentDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "agents/agent_delete.html"