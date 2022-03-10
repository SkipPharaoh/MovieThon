from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.contrib import messages
from .models import Comment, UserProfile
from django.urls import reverse

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

class HomeView(ListView):
    model = Comment
    template_name = 'social.html'

class SocialView(DetailView):
    model = Comment
    template_name = 'social_detail.html'


class AddCommentView(CreateView):
    model = Comment
    fields = ['body']
    template_name = 'add_comment.html'
    success_url = '/social/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddCommentView, self).form_valid(form)

    def get_success_url(self):
        return reverse('social_detail', kwargs={'pk': self.object.pk})
    

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