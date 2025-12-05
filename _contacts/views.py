from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import uuid

from .models import Contact
from .forms import ContactCreateForm, ContactInformationCreateForm

@login_required
def contact_list(request):
    user = request.user
    contact_list = Contact.objects.filter(created_by=user)
    context = {
        "title_action_section": True,
        "page_title": "My contacts",
        "action_menu": [{"name": "Add new", "url": reverse("contact_create")}],
        "obj_list": contact_list
    }
    return render(request, "contacts/contact_list.html", context)

@login_required
def contact_create(request):
    user = request.user
    form = ContactCreateForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        contact = form.save(commit=False)
        contact.created_by = user
        contact.save()
        return redirect("contact_list")
    context = {
        "title_action_section": True,
        "page_title": "Create a new contact",
        "form": form
    }
    return render(request, "contacts/contact_create.html", context)
    
@login_required
def contact_read(request, contact_pk: uuid):
    user = request.user
    contact = get_object_or_404(Contact.objects.prefetch_related("contact_informations"), pk=contact_pk, created_by=user)
    context = {
        "title_action_section": True,
        "page_title": str(contact.name),
        "action_menu": [{"name": "Add information", "url": reverse("contact_information_create", args=[contact_pk])}],
        "obj": contact
        
    }
    return render(request, "contacts/contact_read.html", context)
  
@login_required
def contact_update(request, contact_pk: uuid):
    user = request.user
    contact = get_object_or_404(Contact, pk=contact_pk, created_by=user)
    form = ContactCreateForm(request.POST or None, instance=contact)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("contact_read", contact_pk)
    context = { "obj": contact }
    return render(request, "contacts/contact_read.html", context)

@login_required
def contact_information_create(request, contact_pk: uuid):
    user = request.user
    contact = get_object_or_404(Contact, pk=contact_pk, created_by=user)
    form = ContactInformationCreateForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        contact_information = form.save(commit=False)
        contact_information.created_by = user
        contact_information.contact = contact
        contact_information.save()
        return redirect("contact_read", contact_pk)
    context = {
        "title_action_section": True,
        "page_title": "Add new information",
        "form": form
    }
    return render(request, "contacts/contact_information_create.html", context)