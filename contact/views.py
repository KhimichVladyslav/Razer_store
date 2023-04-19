from django.shortcuts import render
from .models import Contact


def contact(request):
    if request.method == 'POST':
        contact = Contact()
        contact.name = request.POST.get('name')
        contact.email = request.POST.get('email')
        contact.subject = request.POST.get('subject')
        contact.save()
        return render(request, 'contact/contact_done.html')

    return render(request, 'contact/contact.html')
