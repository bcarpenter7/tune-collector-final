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
    context = {
        'title': 'Tune Tracker',
    }
    return render(request, 'home.html', context)

def about(request):
    context = {
        'title': 'About Us',
    }
    return render(request, 'about.html', context)


@login_required
def tunes_index(request):
    is_mobile = False
    if 'Mobile' in request.META['HTTP_USER_AGENT']:
        is_mobile = True

    # get query params, or None
    key = request.GET.get('key')            # A C D G F
    sort = request.GET.get('sort')          # name, key, stars, state?

    tunes = Tune.objects.filter(user=request.user)
    distinct_keys = tunes.values_list('key').order_by('key').distinct()
    avail_keys = [key[0] for key in distinct_keys]

    # dynamic display based on how tunes are displayed
    tunes_heading = ' Tunes'

    if key and len(key) == 1:
        tunes = tunes.filter(key=key.upper())
        tunes_heading = key + tunes_heading
    else:
        tunes_heading = 'All' + tunes_heading

    if sort and sort in ('name', 'stars', 'created_at'):
        if sort == 'stars' or sort == 'created_at':
            tunes = tunes.order_by(f'-{sort}', 'name')
        else:
            tunes = tunes.order_by(sort)
        sort_heading = {
            'name': ' alphabetically',
            'stars': ' by rating',
            'created_at': ' by date',
        }
        tunes_heading += sort_heading[sort]

    return render(request, 'tunes/index.html', {
        'tunes': tunes,
        'title': tunes_heading,
        'avail_keys': avail_keys,
        'is_mobile': is_mobile,
    })


@login_required
def tunes_detail(request, tune_id):
    tune = Tune.objects.get(pk=tune_id)
    context = {
        'tune': tune,
        'title': tune.name
    }
    return render(request, 'tunes/detail.html', context)

class TuneCreate(LoginRequiredMixin, CreateView):
    model = Tune
    form_class = TuneForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create a tune'
        return context

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
    form_class = TuneForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context['title'] = f"Editing {context['tune'].name}"
        return context

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"Deleting {context['tune'].name}"
        return context

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 'Deleted successfully')
        return super().form_valid(form)

    def test_func(self):
        # check to make sure that logged-in user owns the object that they are trying to delete
        obj = Tune.objects.get(pk=self.kwargs['pk'])
        return obj.user == self.request.user
