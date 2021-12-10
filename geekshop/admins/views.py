from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from admins.forms import UserAdminRegisterForm, UserAdminProfileForm, CategoryAdminCreateForm, CategoryAdminUpdateForm, \
    ProductAdminCreateForm, ProductAdminUpdateForm
from authapp.models import User
from mainapp.models import ProductCategory, Product

#user
@user_passes_test(lambda u:u.is_superuser)
def index(request):
    return render(request, 'admins/admin.html')


class UserListView(ListView):
    model = User
    template_name = 'admins/admin-users-read.html'

    def get_context_data(self,*,object_list=None, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Пользователи'
        return context

    @method_decorator(user_passes_test(lambda u:u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)


class UserCreateView(CreateView):
    model = User
    template_name = 'admins/admin-users-create.html'
    form_class = UserAdminRegisterForm
    success_url = reverse_lazy('admins:admin_users')

    def get_context_data(self,*,object_list=None, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Создать пользователя'
        return context

    @method_decorator(user_passes_test(lambda u:u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView, self).dispatch(request, *args, **kwargs)



class UserUpdateView(UpdateView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users')

    def get_context_data(self,*,object_list=None, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Редактирование профиля'
        return context

    @method_decorator(user_passes_test(lambda u:u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserUpdateView, self).dispatch(request, *args, **kwargs)


class UserDeleteView(DeleteView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self,*,object_list=None, **kwargs):
        context = super(UserDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Редактирование профиля'
        return context

    @method_decorator(user_passes_test(lambda u:u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserDeleteView, self).dispatch(request, *args, **kwargs)



class CategoryListView(ListView):
    model = ProductCategory
    template_name = 'admins/admin-categories-read.html'

    def get_context_data(self,*,object_list=None, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Категории'
        return context

    @method_decorator(user_passes_test(lambda u:u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryListView, self).dispatch(request, *args, **kwargs)


class CategoryCreateView(CreateView):
    model = ProductCategory
    template_name = 'admins/admin-categories-create.html'
    form_class = CategoryAdminCreateForm
    success_url = reverse_lazy('admins:admin_categories')

    def get_context_data(self,*,object_list=None, **kwargs):
        context = super(CategoryCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Создать категорию'
        return context

    @method_decorator(user_passes_test(lambda u:u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryCreateView, self).dispatch(request, *args, **kwargs)



class CategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'admins/admin-categories-update-delete.html'
    form_class = CategoryAdminUpdateForm
    success_url = reverse_lazy('admins:admin_categories')

    def get_context_data(self,*,object_list=None, **kwargs):
        context = super(CategoryUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Редактирование категории'
        return context

    @method_decorator(user_passes_test(lambda u:u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryUpdateView, self).dispatch(request, *args, **kwargs)


class CategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'admins/admin-categories-update-delete.html'
    form_class = CategoryAdminUpdateForm
    success_url = reverse_lazy('admins:admin_categories')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self,*,object_list=None, **kwargs):
        context = super(CategoryDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Удаление профиля'
        return context

    @method_decorator(user_passes_test(lambda u:u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryDeleteView, self).dispatch(request, *args, **kwargs)


class ProductListView(ListView):
    model = Product
    template_name = 'admins/admin-products-read.html'

    def get_context_data(self,*,object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['title'] = 'Админка |  Товары'
        return context

    @method_decorator(user_passes_test(lambda u:u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductListView, self).dispatch(request, *args, **kwargs)


class ProductCreateView(CreateView):
    model = Product
    template_name = 'admins/admin-products-create.html'
    form_class = ProductAdminCreateForm
    success_url = reverse_lazy('admins:admin_products')

    def get_context_data(self,*,object_list=None, **kwargs):
        context = super(ProductCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Создать продукт'
        return context

    @method_decorator(user_passes_test(lambda u:u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductCreateView, self).dispatch(request, *args, **kwargs)


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'admins/admin-products-update-delete.html'
    form_class = ProductAdminUpdateForm
    success_url = reverse_lazy('admins:admin_products')

    def get_context_data(self,*,object_list=None, **kwargs):
        context = super(ProductUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Редактирование продукта'
        return context

    @method_decorator(user_passes_test(lambda u:u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductUpdateView, self).dispatch(request, *args, **kwargs)


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'admins/admin-products-update-delete.html'
    form_class = ProductAdminUpdateForm
    success_url = reverse_lazy('admins:admin_products')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self,*,object_list=None, **kwargs):
        context = super(ProductDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Удаление продукта'
        return context

    @method_decorator(user_passes_test(lambda u:u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductDeleteView, self).dispatch(request, *args, **kwargs)


# @user_passes_test(lambda u:u.is_superuser)
# def admin_users(request):
#     context = {
#         'users': User.objects.all(),
#     }
#     return render(request, 'admins/admin-users-read.html', context)

# create on FBV
# @user_passes_test(lambda u:u.is_superuser)
# def admin_users_create(request):
#     if request.method == 'POST':
#         form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_users'))
#     else:
#         form = UserAdminRegisterForm()
#     context = {
#         'title': 'Geekshop - Админ | Регистрация',
#         'form': form,
#     }
#
#     return render(request, 'admins/admin-users-create.html', context)


# @user_passes_test(lambda u:u.is_superuser)
# def admin_users_update(request,pk):
#     user_select = User.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = UserAdminProfileForm(data=request.POST, instance=user_select, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_users'))
#     else:
#         form = UserAdminProfileForm(instance=user_select)
#     context = {
#         'title': 'Geekshop - Админ | Обновление',
#         'form': form,
#         'user_select':user_select,
#     }
#
#     return render(request, 'admins/admin-users-update-delete.html', context)

#
# @user_passes_test(lambda u:u.is_superuser)
# def admin_users_delete(request,pk):
#     if request.method == 'POST':
#         user = User.objects.get(pk=pk)
#         user.is_active = False
#         user.save()
#     return HttpResponseRedirect(reverse('admins:admin_users'))
# @user_passes_test(lambda u:u.is_superuser)
# def admin_categories(request):
#     context = {
#         'categories': ProductCategory.objects.all(),
#     }
#     return render(request, 'admins/admin-categories-read.html', context)

# @user_passes_test(lambda u:u.is_superuser)
# def admin_categories_create(request):
#     if request.method == 'POST':
#         form = CategoryAdminCreateForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_categories'))
#     else:
#         form = CategoryAdminCreateForm()
#     context = {
#         'title': 'Geekshop - Админ | Создание категории',
#         'form': form,
#     }
#
#     return render(request, 'admins/admin-categories-create.html', context)

# @user_passes_test(lambda u:u.is_superuser)
# def admin_categories_update(request, pk):
#     category_select = ProductCategory.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = CategoryAdminUpdateForm(data=request.POST, instance=category_select)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_categories'))
#     else:
#         form = CategoryAdminUpdateForm(instance=category_select)
#     context = {
#         'title': 'Geekshop - Админ | Обновление категории',
#         'form': form,
#         'category_select': category_select,
#     }
#
#     return render(request, 'admins/admin-categories-update-delete.html', context)

# @user_passes_test(lambda u:u.is_superuser)
# def admin_categories_delete(request, pk):
#     if request.method == 'POST':
#         category = ProductCategory.objects.get(pk=pk)
#         category.is_active = False
#         category.save()
#     return HttpResponseRedirect(reverse('admins:admin_categories'))


# @user_passes_test(lambda u:u.is_superuser)
# def admin_products(request):
#     context = {
#         'products': Product.objects.all(),
#     }
#     return render(request, 'admins/admin-products-read.html', context)
#
# @user_passes_test(lambda u:u.is_superuser)
# def admin_products_create(request):
#     if request.method == 'POST':
#         form = ProductAdminCreateForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_products'))
#     else:
#         form = ProductAdminCreateForm()
#
#     context = {
#         'title':'Geekshop - Админ | Создание продукта',
#         'form':form,
#     }
#     return render(request, 'admins/admin-products-create.html', context)
# @user_passes_test(lambda u:u.is_superuser)
# def admin_products_update(request, pk):
#     product_select = Product.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = ProductAdminUpdateForm(data=request.POST, instance=product_select, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_products'))
#     else:
#         form = ProductAdminUpdateForm(instance=product_select)
#
#     context = {
#         'title': 'Geekshop - Админ | Обновление продукта',
#         'form': form,
#         'product_select': product_select,
#     }
#     return render(request, 'admins/admin-products-update-delete.html', context)

# @user_passes_test(lambda u:u.is_superuser)
# def admin_products_delete(request,pk):
#     if request.method == 'POST':
#         product = Product.objects.get(pk=pk)
#         product.is_active = False
#         product.save()
#     return HttpResponseRedirect(reverse('admins:admin_products'))



