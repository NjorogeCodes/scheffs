from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def services(request):
    return render(request, 'service.html')
def menu(request):
    return render(request, 'menu.html')
def booking(request):
    return render(request, 'booking.html')
def team(request):
    return render(request, 'team.html')
def testimonial(request):
    return render(request, 'testimonial.html')
def contact(request):
    return render(request, 'contact.html')





