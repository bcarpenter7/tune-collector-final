from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import TuneForm
from .models import Tune
from django.urls import reverse_lazy

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def tunes_index(request):
    tunes = Tune.objects.filter(user=request.user).order_by('name')
    distinct_keys = tunes.values_list('key').order_by('key').distinct()
    avail_keys = [key[0] for key in distinct_keys]
    return render(request, 'tunes/index.html', {
        'tunes': tunes,
        'title': 'All',
        'avail_keys': avail_keys,
    })

@login_required
def tunes_detail(request, tune_id):
    tune = Tune.objects.get(pk=tune_id)
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
        messages.add_message(self.request, messages.SUCCESS, 'Created successfully')
        return redirect(self.get_success_url())


class TuneUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Tune
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('tune:detail', kwargs={'tune_id': self.object.pk})

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 'Updated successfully')
        return super().form_valid(form)

    def test_func(self):
        # check to make sure that logged-in user owns the object that they are trying to delete
        obj = Tune.objects.get(pk=self.kwargs['pk'])
        return obj.user == self.request.user

class TuneDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Tune
    success_url = '/tunes'

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 'Deleted successfully')
        return super().form_valid(form)

    def test_func(self):
        # check to make sure that logged-in user owns the object that they are trying to delete
        obj = Tune.objects.get(pk=self.kwargs['pk'])
        return obj.user == self.request.user

@login_required
def tunes_note_filter(request, char):
    tunes = Tune.objects.filter(user=request.user).order_by('name')
    distinct_keys = tunes.values_list('key').order_by('key').distinct()
    avail_keys = [key[0] for key in distinct_keys]

    if len(char) == 1:
        tunes = tunes.filter(key__iexact=char)

    context = {
        'tunes': tunes,
        'title': char.upper(),
        'avail_keys': avail_keys,
    }
    return render(request, 'tunes/index.html', context)
