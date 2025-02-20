from django.shortcuts import render,get_object_or_404,redirect
from contact.models import Contact
from django.db.models import Q

# Create your views here.
def index(request):

    contacts = Contact.objects \
        .filter(show=True)\
        .order_by('-id')[10:20]
    
    context = {
        'contacts': contacts,
        'site_title': 'Contatos -'
    }

    return render(
        request,
        'contact/index.html',
        context
    )

def contact(request, contact_id):

    # single_contact = Contact.objects.filter(pk=contact_id).first()
    single_contact = get_object_or_404(
        Contact.objects.filter(pk=contact_id, show=True))

    context = {
        'contact': single_contact,
        'site_title': f'{single_contact.first_name} {single_contact.last_name} - '
    }

    return render(
        request,
        'contact/contact.html',
        context
    )

def search(request):

    search_value = request.GET.get('q', '').strip()

    if not search_value:
        return redirect('contact:index')

    contacts = Contact.objects \
        .filter(show=True)\
        .filter(
            Q(first_name__icontains=search_value) |
            Q(last_name__icontains=search_value)
            ) \
        .order_by('-id')
    
    context = {
        'contacts': contacts,
        'site_title': 'Contatos -'
    }

    return render(
        request,
        'contact/index.html',
        context
    )