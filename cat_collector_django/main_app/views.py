from django.shortcuts import render

# Create your views here.
# Step 2: Create the anticipated views function

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')