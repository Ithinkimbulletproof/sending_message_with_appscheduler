from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Client, Message, Mailing, MailingAttempt
from .forms import ClientForm, MessageForm, MailingForm, MailingAttemptForm


class ClientListView(ListView):
    model = Client
    template_name = "mailings/client_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["additional_info"] = "Some additional information"
        return context


class ClientDetailView(DetailView):
    model = Client
    template_name = "mailings/client_detail.html"


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = "mailings/client_form.html"


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = "mailings/client_form.html"


class ClientDeleteView(DeleteView):
    model = Client
    template_name = "mailings/client_confirm_delete.html"
    success_url = reverse_lazy("client_list")


class MessageListView(ListView):
    model = Message
    template_name = "mailings/message_list.html"


class MessageDetailView(DetailView):
    model = Message
    template_name = "mailings/message_detail.html"


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = "mailings/message_form.html"


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    template_name = "mailings/message_form.html"


class MessageDeleteView(DeleteView):
    model = Message
    template_name = "mailings/message_confirm_delete.html"
    success_url = reverse_lazy("message_list")


class MailingListView(ListView):
    model = Mailing
    template_name = "mailings/mailing_list.html"


class MailingDetailView(DetailView):
    model = Mailing
    template_name = "mailings/mailing_detail.html"


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    template_name = "mailings/mailing_form.html"


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    template_name = "mailings/mailing_form.html"


class MailingDeleteView(DeleteView):
    model = Mailing
    template_name = "mailings/mailing_confirm_delete.html"
    success_url = reverse_lazy("mailing_list")


class MailingAttemptListView(ListView):
    model = MailingAttempt
    template_name = "mailings/mailingattempt_list.html"


class MailingAttemptDetailView(DetailView):
    model = MailingAttempt
    template_name = "mailings/mailingattempt_detail.html"


class MailingAttemptCreateView(CreateView):
    model = MailingAttempt
    form_class = MailingAttemptForm
    template_name = "mailings/mailingattempt_form.html"


class MailingAttemptUpdateView(UpdateView):
    model = MailingAttempt
    form_class = MailingAttemptForm
    template_name = "mailings/mailingattempt_form.html"


class MailingAttemptDeleteView(DeleteView):
    model = MailingAttempt
    template_name = "mailings/mailingattempt_confirm_delete.html"
    success_url = reverse_lazy("mailingattempt_list")
