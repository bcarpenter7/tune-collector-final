from django.contrib import messages
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
    return render(request, 'about.html')

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
        messages.add_message(self.request, messages.SUCCESS, 'Created successfully')
        return redirect(self.get_success_url())


class TuneUpdate(LoginRequiredMixin, UpdateView):
    model = Tune
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('tune:detail', kwargs={'tune_id': self.object.pk})

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 'Updated successfully')
        return super().form_valid(form)


class TuneDelete(LoginRequiredMixin, DeleteView):
    model = Tune
    success_url = '/tunes'

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 'Deleted successfully')
        return super().form_valid(form)

@login_required
def tunes_note_filter(request, char):
    tunes = Tune.objects.filter(key__iexact=char, user=request.user).order_by('name')
    context = {
        'tunes': tunes,
        'title': char.upper()
    }
    if len(char) > 1:
        context['title'] = f'{char} is an invalid selection for '
    return render(request, 'tunes/index.html', context)
