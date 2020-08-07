from django.shortcuts import render

# Create your views here.

def home(request):
    """
    Home page for blogs site
    """
    context = {}
    return render(request, 'ghosts/index.html', context)
