# Create your views here.
import random

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView

from users.forms import UserForm, VerificationForm
from users.models import User


class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        generate_code = ''.join([str(random.randint(0, 9)) for _ in range(12)])
        user.verification_code = generate_code
        user.save()

        # Отправляем письмо с кодом активации
        send_mail(
            subject='Код верификации',
            message=f'Пожалуйста, для вашей верификации и активации аккаунта введите код: {generate_code}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return redirect(reverse('users:confirming', kwargs={'pk': user.pk}))


class UserVerifyView(View):
    template_name = 'users/email_confirmed.html'

    def get(self, request, *args, **kwargs):
        form = VerificationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = VerificationForm(request.POST)
        if form.is_valid():
            print("First")
            entered_code = form.cleaned_data['verify_code']
            user_pk = kwargs.get('pk')
            user = get_object_or_404(User, pk=user_pk)
            print(entered_code)
            print(user.verification_code)
            print(entered_code == user.verification_code)

            if entered_code == user.verification_code:
                print("Second")

                user.is_active = True
                user.verified = True
                user.save()
                messages.success(request, 'Аккаунт успешно активирован!')
                return redirect(reverse('users:login'))
            else:
                messages.error(request, 'Неверный код верификации. Попробуйте снова.')

        return render(request, self.template_name, {'form': form})
