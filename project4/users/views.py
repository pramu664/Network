from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse

from .forms import UserRegisterForm

# Register a new user
def register(request):

    # check if method is POST
    if request.POST:

        # Take in the data that user submitted and save it as register form
        register_form = UserRegisterForm(request.POST)

        # Check if form data is valid(server-side)
        if register_form.is_valid():

            # Save the user to database
            register_form.save()

            # Isolate the username from the 'cleaned' version of form data
            username = register_form.cleaned_data.get("username")

            # Create a success message for current request
            messages.success(request, f"Welcome {username}")

            # Redirect the user to the list of posts
            return HttpResponseRedirect(reverse('index'))

        else:

            # If the form is invlid, re-render the register page with existing information.
            return render(request, "users/register.html", {"register_form": register_form})

    # if the method is Get, render the register page with empty form
    return render (request, "users/register.html", {"register_form": UserRegisterForm()})

def profile(request):
    return render(request, 'users/profile.html')
