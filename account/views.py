from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from tune.models import Tune
from .forms import RegistrationForm
from .models import MyUser


def user_registration_view(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.set_password(form.cleaned_data['password2'])
            user.save()
            messages.add_message(request, messages.SUCCESS, 'Account created, please log in')
            return redirect(reverse_lazy('account:login'))
    else:
        form = RegistrationForm()

    context = {
        'form': form
    }
    return render(request, 'account/registration/register.html', context)


def user_deletion_view(request):
    if not request.user.is_authenticated:
        return redirect('/')
    return render(request, 'account/delete.html')


def user_deletion_confirm(request):
    if request.user.is_authenticated:
        request.user.is_active = False
        request.user.save()
        messages.add_message(request, messages.SUCCESS, 'Account deleted')
        return redirect('/')


@login_required
def index_view(request):
    # get all active users other than currently logged-in
    users = MyUser.objects.filter(~Q(pk=request.user.pk), is_active=True)

    # get filter param, or None
    username = request.POST.get('username')
    if username:
        users = users.filter(username__contains=username)

    users = users.order_by('username')

    context = {
        'users': users,
    }
    return render(request, 'account/index.html', context)


@login_required
def detail_view(request, pk):
    is_mobile = False
    if 'Mobile' in request.META['HTTP_USER_AGENT']:
        is_mobile = True

    # get query params, or None
    key = request.GET.get('key')
    sort = request.GET.get('sort')

    user = MyUser.objects.get(pk=pk)
    tunes = Tune.objects.filter(user=user).order_by('name')
    distinct_keys = tunes.values_list('key').order_by('key').distinct()
    avail_keys = [key[0] for key in distinct_keys]

    if key and len(key) == 1:
        tunes = tunes.filter(key=key.upper())

    if sort and sort in ('name', 'stars', 'created_at'):
        if sort == 'stars' or sort == 'created_at':
            tunes = tunes.order_by(f'-{sort}', 'name')
        else:
            tunes = tunes.order_by(sort)

    context = {
        'user': user,
        'tunes': tunes,
        'title': 'All',
        'avail_keys': avail_keys,
        'is_mobile': is_mobile,
    }
    return render(request, 'account/detail.html', context)
