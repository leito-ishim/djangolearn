from django.conf import settings
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, FormView

from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from authapp.models import User
from baskets.models import Basket


# def login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#             user = auth.authenticate(username=username,password=password)
#             if user.is_active:
#                 auth.login(request,user)
#                 return HttpResponseRedirect(reverse('index'))
#         else:
#             print(form.errors)
#     else:
#         form = UserLoginForm()
#     context = {
#         'title': 'Geekshop | Авторизация',
#         'form': form,
#     }
#
#     return render(request, 'authapp/login.html', context)
from mainapp.mixin import BaseClassContextMixin, UserDispatchMixin


class LoginListView(LoginView, BaseClassContextMixin):
    template_name = 'authapp/login.html'
    form_class = UserLoginForm
    title = 'Geekshop | Авторизация'


class RegisterlistView(FormView, BaseClassContextMixin):
    model = User
    template_name = 'authapp/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('authapp:login')
    title = 'Geekshop | Регистрация'

    def post(self, request, *args, **kwargs):

        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = form.save()
            if self.send_verify_link(user):
                messages.set_level(request, messages.SUCCESS)
                messages.success(request, 'Вы успешно зарегистрировались!')
                return HttpResponseRedirect(reverse('authapp:login'))
            else:
                messages.set_level(request, messages.ERROR)
                messages.error(request, form.errors)
        else:
            messages.set_level(request, messages.ERROR)
            messages.error(request, form.errors)
        return render(request, self.template_name, {'form':form})


    def send_verify_link(self, user):
        verify_link = reverse('authapp:verify', args=[user.email, user.activation_key])
        subject = f'Для активации учетной записи {user.username} пройдите по ссылке'
        message = f'Для подтверждения учетной записи {user.username} на портале \n {settings.DOMAIN_NAME}{verify_link}'
        return send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)



    def verify(self, email, activate_key):
        try:
            user = User.objects.get(email=email)
            if user and user.activation_key == activate_key and not user.is_activation_key_expires():
                user.activation_key = ''
                user.activation_key_expires = None
                user.is_active = True
                user.save()
                auth.login(self, user)
            return render(self, 'authapp/verification.html')
        except Exception as e:
            return HttpResponseRedirect(reverse('index'))



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

class ProfileFormView(UpdateView, BaseClassContextMixin, UserDispatchMixin):
    template_name = 'authapp/profile.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('authapp:profile')
    success_message = 'Ok'
    title = 'Geekshop | Профиль'

    def get_object(self, *args, **kwargs):
        return get_object_or_404(User, pk=self.request.user.pk)

    # def get_context_data(self, **kwargs):
    #     context = super(ProfileFormView, self).get_context_data(**kwargs)
    #     context['baskets'] = Basket.objects.filter(user=self.request.user)
    #     return context

    # @method_decorator(login_required)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(UserUpdateView, self).dispatch(request, *args, **kwargs)


# def logout(request):
#     auth.logout(request)
#     return render(request, 'mainapp/index.html')

class Logout(LogoutView):
    template_name = 'mainapp/index.html'






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