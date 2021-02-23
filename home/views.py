from django.shortcuts import render
from .models import Contact, Contactinformation,testimonial


# Create your views here.
def home(request):
    view = {}
    view['review'] = testimonial.objects.all()
    return render(request,'index.html',view)

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def price(request):
    return render(request,'price.html')

def portfolio(request):
    return render(request,'portfolio.html')

def elements(request):
    return render(request,'elements.html')

def contact(request):
    view = {}
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        data = Contact.objects.create(
            name = name,
            email = email,
            subject = subject,
            message = message
        )
        data.save()
        view['SUCCESS'] = 'Data has been saved successfully'

    view['info'] = Contactinformation.objects.all()
    return render(request,'contact.html',view)

