from re import template
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# IMPORTS RELATED TO SIGNUP
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Authorization decorators:
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.


# VIEWS #

# Home
class Home(TemplateView):
    template_name="home.html"

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
            return redirect('artist_list')
        else:

            context = {'form': form}
            return render(request, "registration/signup.html", context)