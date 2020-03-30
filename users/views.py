from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.contrib.auth.views import PasswordChangeView, PasswordResetView

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class UserUpdateView(generic.UpdateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('index')
    template_name = 'update.html'

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return CustomUser.objects.all()
        else:
            return CustomUser.objects.filter(id=user.id)

class UserPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('index')
    template_name = 'change_password.html'

class UserPasswordResetView(PasswordResetView):
    success_url = reverse_lazy('login')
    template_name = 'reset_password.html'

class UserRegistrationView(generic.base.TemplateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('index')
    template_name = 'registration.html'