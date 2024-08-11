from django.shortcuts import render, get_object_or_404, redirect
from .models import Mailing
from .forms import MailingForm

def mailing_list(request):
    mailings = Mailing.objects.all()
    return render(request, 'mailings/mailing_list.html', {'mailings': mailings})

def mailing_detail(request, pk):
    mailing = get_object_or_404(Mailing, pk=pk)
    return render(request, 'mailings/mailing_detail.html', {'mailing': mailing})

def mailing_create(request):
    if request.method == "POST":
        form = MailingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mailing_list')
    else:
        form = MailingForm()
    return render(request, 'mailings/mailing_form.html', {'form': form})

def mailing_edit(request, pk):
    mailing = get_object_or_404(Mailing, pk=pk)
    if request.method == "POST":
        form = MailingForm(request.POST, instance=mailing)
        if form.is_valid():
            form.save()
            return redirect('mailing_list')
    else:
        form = MailingForm(instance=mailing)
    return render(request, 'mailings/mailing_form.html', {'form': form})

def mailing_delete(request, pk):
    mailing = get_object_or_404(Mailing, pk=pk)
    if request.method == "POST":
        mailing.delete()
        return redirect('mailing_list')
    return render(request, 'mailings/mailing_confirm_delete.html', {'mailing': mailing})
