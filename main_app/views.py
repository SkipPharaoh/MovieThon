from re import template
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.contrib import messages

# IMPORTS RELATED TO SIGNUP
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Authorization decorators:
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# from .models import UserProfile
# from .models import Comments

# VIEWS #

# Home
class Home(TemplateView):
    template_name="home.html"

# Watchlist
class Watchlist(TemplateView):
    template_name="watchlist.html"


# Profile
class Profile(TemplateView):
    # def get(self, request, pk, *args, **kwargs):


    
    template_name="profile.html" 


# Signup
class Signup(View):
    # get request
    def get(self, request):
        form = UserCreationForm() # comes from the auth.forms library - create a new form;

        context = {'form': form}
        return render(request, "registration/signup.html", context)


    # post request
    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save() # save the user in the users table
            # login functionality
            login(request, user)
            return redirect('home')
        else:

            context = {'form': form}
            return render(request, "registration/signup.html", context)




# Login
# def login_user(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')

#         else:
#             messages.success(request, ("There Was An Error Logging In, Try Again..."))
#             return redirect('login')
        
#     else:
#         return render(request, 'registration/login.html', )
