from django.shortcuts import render,redirect
from .forms import ContactForm
# Create your views here.
def show(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        
        if form.is_valid():
            print("FROM WAS VALID! ")
            
            return redirect('show')
    else:
        form=ContactForm()
       
    return render(request,'contact/index.html',{
        'form':form
        
    })