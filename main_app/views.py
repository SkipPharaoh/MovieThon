from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.contrib import messages
from .models import Comment, UserProfile
from django.urls import reverse
from .forms import CommentForm

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
    playing = requests.get(f"https://api.themoviedb.org/3/movie/now_playing?api_key={TMDB_API_KEY}&language=en-US&page={page}").json()

    coming = requests.get(f"https://api.themoviedb.org/3/movie/upcoming?api_key={TMDB_API_KEY}&language=en-US&page={page}").json()

    trending = requests.get(f"https://api.themoviedb.org/3/trending/all/day?api_key={TMDB_API_KEY}").json()
    return render(request, 'home.html', {'res': playing, 'coming': coming, 'trend': trending})

class HomeView(ListView):
    model = Comment
    template_name = 'social.html'


@method_decorator(login_required, name="dispatch")
class SocialView(DetailView):
    model = Comment
    template_name = 'social_detail.html'



@method_decorator(login_required, name="dispatch")
class AddComment(CreateView):
    model = Comment
    form_class = CommentForm
    # fields = ['body']
    template_name = 'add_comment.html'
    success_url = '/social/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddComment, self).form_valid(form)

    def get_success_url(self):
        return reverse('social_detail', kwargs={'pk': self.object.pk})
    


@method_decorator(login_required, name="dispatch")
class UpdateComment(UpdateView):
    model = Comment
    template_name = 'update_comment.html'
    # fields = ['body']
    form_class = CommentForm
    success_url = '/'



@method_decorator(login_required, name="dispatch")
class DeleteComment(DeleteView):
    model = Comment
    template_name = 'delete_comment.html'
    success_url = '/'


def LikeView(request, pk):
    comment = get_object_or_404(Comment, id=request.POST.get('comment_id'))
    comment.likes.add(request.user)
    return HttpResponseRedirect(reverse('social_detail', args=[str(pk)]))







@method_decorator(login_required, name="dispatch")
class MovieDetail(TemplateView):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('movie_id')
        info = requests.get(f"https://api.themoviedb.org/3/movie/{id}?api_key={TMDB_API_KEY}").json()
        return render(request, 'movie_detail.html', {'info': info})
    # template_name = "movie_detail.html"

                        # USER MODEL #
# Watchlist

@method_decorator(login_required, name="dispatch")
class Watchlist(TemplateView):
    template_name="watchlist.html"


# Profile

@method_decorator(login_required, name="dispatch")
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