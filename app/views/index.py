from django.shortcuts import render

from app.common.budget import calculate_budget_left
from app.models import Profile, Expense
from app.views.profiles import create_profile


def index(request):
    if Profile.objects.exists():
        expenses = Expense.objects.all()
        profile = Profile.objects.all()[0]
        profile.budget_left = calculate_budget_left(profile, expenses)
        context = {
            'profile': profile,
            'expenses': expenses,
        }
        return render(request, 'home-with-profile.html', context)
    else:
        return create_profile(request)
