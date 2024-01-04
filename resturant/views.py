from django.shortcuts import render , redirect
from .froms import BookForm
from .models import Book , Menu as MenuModel

def home (request):
    return render(request, 'home.html', )

def booking(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_now')  
    else:
        form = BookForm()

    context = {"form": form}
    return render(request, 'book.html', context)

def aboutus(request):
    return render(request,'aboutus.html')

def Menu(request): 
    m = MenuModel.objects.all()
    
    context = { 'menu':m }


    return render(request , 'Menu.html' , context)