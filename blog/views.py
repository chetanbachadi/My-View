from django.shortcuts import render, redirect
from .models import Blog
from .models import Contact

def home(request):
   return render(request, 'home.html')

def about(request):
    return render(request, 'aboutus.html')

def contact(request):
    submitted = False
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        opinion = request.POST.get('opinion')

        # Save to DB
        Contact.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            opinion=opinion,
        )
        submitted = True

    return render(request, 'contact.html', {'submitted': submitted})



def footer(request):
    return render(request, 'footer.html')

def blog(request):
    blogs = Blog.objects.all().order_by('-created_at')  # Fetch all blog posts
    return render(request, 'blog.html', {'blogs': blogs})

