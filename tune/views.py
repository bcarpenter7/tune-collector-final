from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import TuneForm
from .models import Tune
from django.urls import reverse_lazy
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html' )

@login_required
def tunes_index(request):
    tunes = Tune.objects.filter(user=request.user).order_by('name')
    return render(request, 'tunes/index.html', {
        'tunes': tunes,
        'title': 'All'
    })

@login_required
def tunes_detail(request, tune_id):
    tune = Tune.objects.get(pk=tune_id, user=request.user)
    return render(request, 'tunes/detail.html', {
        'tune': tune
    })

class TuneCreate(LoginRequiredMixin, CreateView):
    model = Tune
    form_class = TuneForm

    def get_success_url(self):
        return reverse_lazy('tune:detail', kwargs={'tune_id': self.object.pk})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return redirect(self.get_success_url())


class TuneUpdate(LoginRequiredMixin, UpdateView):
    model = Tune
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('tune:detail', kwargs={'tune_id': self.object.pk})

class TuneDelete(LoginRequiredMixin, DeleteView):
    model = Tune
    success_url = '/tunes'



# EXPERIMENTAL DOWN HERE

@login_required
def tunes_index_d(request):
    tunes = Tune.objects.filter(key='D', user=request.user).order_by('name')
    return render(request, 'tunes/index.html', {
        'tunes': tunes,
        'title': 'D'
    })

@login_required
def tunes_index_a(request):
    tunes = Tune.objects.filter(key='A', user=request.user).order_by('name')
    return render(request, 'tunes/index.html', {
        'tunes': tunes,
        'title': 'A'
    })

@login_required
def tunes_index_g(request):
    tunes = Tune.objects.filter(key='G', user=request.user).order_by('name')
    return render(request, 'tunes/index.html', {
        'tunes': tunes,
        'title': 'G'
    })

@login_required
def tunes_index_c(request):
    tunes = Tune.objects.filter(key='C', user=request.user).order_by('name')
    return render(request, 'tunes/index.html', {
        'tunes': tunes,
        'title': 'C'
    })