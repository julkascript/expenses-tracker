from django.shortcuts import render, redirect

from app.common.budget import calculate_budget_left
from app.forms.profile import ProfileForm
from app.models import Profile, Expense


def profile_index(request):
    expenses = Expense.objects.all()
    profile = Profile.objects.all()[0]
    profile.budget_left = calculate_budget_left(profile, expenses)
    context = {
        'profile': profile,
    }
    return render(request, 'profile.html', context)


def create_profile(request):
    if request.method == 'GET':
        context = {
            'form': ProfileForm(),
        }
        return render(request, 'home-no-profile.html', context)
    form = ProfileForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {
        'form': form,
    }
    return render(request, 'home-no-profile.html', context)


def edit_profile(request):
    profile = Profile.objects.all()[0]
    if request.method == 'GET':
        context = {
            'form': ProfileForm(instance=profile)
        }
        return render(request, 'profile-edit.html', context)
    form = ProfileForm(request.POST, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('profile index')
    context = {
        'form': form,
    }
    return render(request, 'profile-edit.html', context)


def delete_profile(request):
    profile = Profile.objects.all()[0]
    if request.method == 'GET':
        context = {
            'form': ProfileForm(instance=profile),
        }
        return render(request, 'profile-delete.html', context)
    profile.delete()
    [expense.delete() for expense in Expense.objects.all()]
    return redirect('index')
