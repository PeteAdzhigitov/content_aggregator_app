from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import UserRegisterForm


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request,f"Account has been successfully created for {username}! Log in again")
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request,'register.html',{"form":form})

