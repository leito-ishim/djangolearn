from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect

from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from authapp.models import User
from baskets.models import Basket


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username,password=password)
            if user.is_active:
                auth.login(request,user)
                return HttpResponseRedirect(reverse('index'))
        else:
            print(form.errors)
    else:
        form = UserLoginForm()
    context = {
        'title': 'Geekshop | Авторизация',
        'form': form,
    }

    return render(request, 'authapp/login.html', context)



class UserRegistrationCreateView(CreateView):
    model = User
    template_name = 'authapp/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('authapp:login')

    def get_context_data(self,*,object_list=None, **kwargs):
        context = super(UserRegistrationCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Geekshop | Регистрация'
        return context


# @login_required
# def profile(request):
#     if request.method == 'POST':
#         form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
#         if form.is_valid():
#             messages.set_level(request, messages.SUCCESS)
#             messages.success(request, 'Изменения сохранены')
#             form.save()
#         else:
#             messages.set_level(request, messages.ERROR)
#             messages.error(request, form.errors)
#
#     context = {
#         'title': 'Geekshop | Профайл',
#         'form': UserProfileForm(instance=request.user),
#         'baskets': Basket.objects.filter(user=request.user)
#     }
#     return render(request, 'authapp/profile.html', context)

class UserUpdateView(UpdateView):
    model = User
    template_name = 'authapp/profile.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('authapp:profile')

    def get_context_data(self,*,object_list=None, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Профайл'
        return context

    # @method_decorator(login_required)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(UserUpdateView, self).dispatch(request, *args, **kwargs)


def logout(request):
    auth.logout(request)
    return render(request, 'mainapp/index.html')






# def registration(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request,'Вы успешно зарегистрировались')
#             return HttpResponseRedirect(reverse('authapp:login'))
#         # else:
#         #     print(form.errors)
#     else:
#         form = UserRegisterForm()
#
#     context = {
#         'title': 'Geekshop | Регистрация',
#         'form': form
#     }
#     return render(request, 'authapp/register.html', context)