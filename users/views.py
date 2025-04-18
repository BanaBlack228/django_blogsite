from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm, NewRegistrationForm



def register(request):
    # Когда отправляем заполненую форму на сервер
    if request.method == "POST":
        # Создаем объект формы с данными из запроса
        form = NewRegistrationForm(request.POST)
        # Если форма валидна
        if form.is_valid():
            # Создаем объект пользователя без записи в БД
            new_user = form.save(commit=False)
            # Хэшируем пароль при помощи set_password
            new_user.set_password(form.cleaned_data['password'])
            # Сохраняем пользователя и БД
            new_user.save()
            context = {"title": "Регистрация завершена", "new_user":new_user}
            return render(request,template_name="users/registration_done.html", context=context)
    # Если метод GET(страница с пустой формой регистрации)
    form = NewRegistrationForm()
    context = {"title": "Регистрация пользователя", "register_form":form}
    return render(request,template_name="users/registration.html", context=context)


def log_in(request):
    pass

def log_out(request):
    pass

def user_profile(request, pk):
    pass


