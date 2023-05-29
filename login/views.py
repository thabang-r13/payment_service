from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .forms import SignUpForm

# Create your views here.
#def login(request):
#  template = loader.get_template('signup.html')
#  return HttpResponse(template.render())


# views.py
#def login(request):
#    if request.method == 'POST':
#        form = SignUpForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('user_portal')
#    else:
#        form = SignUpForm()
#    return render(request, 'signup.html', {'form': form})

#def login(request):
#    return render(request, 'signup.html')

# This is the working code. Do not change! It is the sign-up view
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_portal')
        else:
            # Handle form validation errors
            print(form.errors)
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import User

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user_profile = User.objects.get(email=email)
                if user_profile.password == password:
                    # Credentials are valid, redirect to success page
                    return redirect('user_portal')
                else:
                    form.add_error('password', 'Incorrect password')
            except User.DoesNotExist:
                form.add_error('email', 'User does not exist')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


