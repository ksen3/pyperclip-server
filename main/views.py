from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .forms import RegisterForm, LoginForm
from .serializers import *


class DataAddAPIView(generics.CreateAPIView):
    serializer_class = DataSerializer
    queryset = Data.objects.all()


class DataRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = DataSerializer
    queryset = Data.objects.all()
    permission_classes = (IsAdminUser,)


class DataListAPIView(generics.ListAPIView):
    serializer_class = DataSerializer
    queryset = Data.objects.all()
    permission_classes = (IsAdminUser, )

# ----------


class Details(LoginRequiredMixin, ListView):
    queryset = Data.objects.all()
    template_name = 'main/details.html'
    login_url = 'index'
    redirect_field_name = 'index'
    paginate_by = 15
    context_object_name = 'list'


class DetailView(DetailView):
    model = Data
    template_name = 'main/detail_view.html'
    success_url = reverse_lazy('index')


def logout_user(request):
    logout(request)
    return redirect('index')


class RegisterUser(SuccessMessageMixin, CreateView):
    template_name = 'main/register.html'
    success_url = reverse_lazy('index')
    form_class = RegisterForm
    success_message = 'Вы успешно прошли регистрацию. Теперь вы можете войти как пользователь.'



class LoginUser(SuccessMessageMixin, LoginView):
    form_class = LoginForm
    template_name = 'main/index.html'

    def get_success_url(self):
        return reverse_lazy('details')
