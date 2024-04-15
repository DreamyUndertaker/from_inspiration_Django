from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from registration.forms import SignupForm, SigninForm  # Подключаем форму для аутентификации


from django.contrib import messages


def signUp(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)
                return redirect('home')
            except Exception as e:
                messages.error(request, f"An error occurred while signing up: {e}")
                return redirect('signup')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
            return redirect('signup')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})


def signIn(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)  # Используем форму для аутентификации
        print(form.is_valid())
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                print(user)
                login(request, user)
                return redirect('home')
            else:
                error_message = 'Invalid login credentials.'
                return render(request, 'registration/signin.html', {'form': form, 'error_message': error_message})
    else:
        form = SigninForm()  # Используем форму для аутентификации
    return render(request, 'registration/signin.html', {'form': form})
