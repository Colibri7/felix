from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse


def password_change(request):
    messages.add_message(request, messages.INFO, 'Password changes successfully')
    return redirect(reverse('profile:home'))




