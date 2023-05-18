from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method != "POST":
        form = UserCreationForm()

    else:
        # Обробка заповненої форми
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Здійснення входу та перенаправлення на домашню сторінку
            login(request, new_user)
            return redirect('store:all_products')

        # Вивести пусту або недіючу форму.
    context = {'form': form}

    return render(request, 'registration/register.html', context)
