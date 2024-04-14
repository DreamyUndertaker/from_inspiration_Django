from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from registration.forms import SignupForm


def signUp(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})


def signIn(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        print('0')
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                # Redirect to a success page.
                print('1')
                return redirect('home')
            else:
                # Return an 'invalid login' error message.
                print('2')
                return render(request, 'registration/signin.html', {'form': form, 'error_message': 'Invalid login credentials.'})
    else:
        form = SignupForm()
        print("error")

    return render(request, 'registration/signin.html', {'form': form})



