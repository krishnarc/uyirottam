from django.shortcuts import render
from Blood_app.forms import Add_donors_form
# Create your views here.
def index(request):
    return render(request,"Blood_app/index.html")

def Sign_up(request):
    form = Add_donors_form()

    if request.method =='POST':
        form = Add_donors_form(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("It is not valid..!! please verify")

    return render(request,"Blood_app/signup.html",{'form':form})
