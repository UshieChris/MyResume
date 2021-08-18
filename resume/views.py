from django.shortcuts import render
from django.http import HttpResponse
from . models import Contact

# Create your views here.
def index(request):
    return render (request, 'index.html')

def personal(request):
    name = request.POST['name']
    subject = request.POST['subject']
    email = request.POST['email']
    message = request.POST['message']

    Details = Contact.objects.create(name = name, text = subject, email = email, message = message)
    Details.save()

    return render( request, 'person.html')