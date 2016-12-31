from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from recommendation_engine.forms import UserForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse


# This file defines the view logic of the web application user interfaces.

@login_required
def frontpage(request):
    return render(request, 'recommendation_engine/templates/front_page.html', {})


@login_required
def profile(request):
    return render(request, 'recommendation_engine/templates/profile_page.html', {})


def register(request):
    # Flag to indicate the outcome of the registration
    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            # Update the flag upon successful registration
            registered = True

            # TODO: CONFIRMATION EMAIL PAGE

        else:
            print(user_form.errors)

    else:
        # If the HTTP POST method is not used, new form rendered ready for user input
        user_form = UserForm()

    # Render the template depending on the context.
    return render(request, 'recommendation_engine/templates/user_registration.html',
                  {'user_form': user_form, 'registered': registered})


def user_login(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/recommendation_engine/')
            else:
                return render(request, 'recommendation_engine/templates/user_login.html',
                              {'error_message': "Your SocialNews account has been disabled."})
        else:
            return render(request, 'recommendation_engine/templates/user_login.html',
                          {'error_message': "Invalid login credentials supplied."})
    else:
        return render(request, 'recommendation_engine/templates/user_login.html', {})


@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect('/recommendation_engine/')
