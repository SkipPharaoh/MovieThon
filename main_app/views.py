from re import template
from xml.etree.ElementTree import Comment
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.contrib import messages
from .models import Comment, UserProfile

# IMPORTS RELATED TO SIGNUP
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Authorization decorators:
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Import For Fetch
import requests
import os
from dotenv import load_dotenv
load_dotenv()


TMDB_API_KEY = os.getenv('TMDB_API_KEY')
page = 1

# VIEWS #
                        # Movies #
# Home
    # FETCH REQUEST #
def home(request):
    data = requests.get(f"https://api.themoviedb.org/3/movie/now_playing?api_key={TMDB_API_KEY}&language=en-US&page={page}").json()
    return render(request, 'home.html', {'res': data})


class MovieDetail(TemplateView):
    template_name = "movie_detail.html"

                        # USER MODEL #
# Watchlist
class Watchlist(TemplateView):
    template_name="watchlist.html"


# Profile
class Profile(TemplateView):
    def get(self, request, pk, *args, **kwargs):
        return render(request, 'profile.html' )



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