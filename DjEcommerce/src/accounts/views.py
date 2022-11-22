from django.shortcuts import render, HttpResponseRedirect
from accounts.models import UserRegisterForm


def register_view(request):
    register_form = UserRegisterForm()
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        print(username)
        print(email)
        print(password)
        return HttpResponseRedirect('/')

    context = {
        'register_form': register_form
    }

    return render(request, 'accounts/register.html', context)
