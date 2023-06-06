from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.forms import EmailField
from django.utils.translation import gettext_lazy as _
from django import forms
from .models import Especialidade, Clinica, Medico, Consulta
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
User = get_user_model()

class UserSignupForm(UserCreationForm):
    cpf = forms.CharField(label="CPF", max_length=11)
    data_nascimento = forms.DateField(label="Data de Nascimento", widget=forms.DateInput(attrs={'type': 'date'}))
    endereco = forms.CharField(label="Endereço")
    username = forms.CharField(label="Username")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise ValidationError("Username already exists.")
        return username

    def save(self, commit=True):
        user = super().save(commit=False)
        user.cpf = self.cleaned_data.get("cpf")
        user.data_nascimento = self.cleaned_data.get("data_nascimento")
        user.endereco = self.cleaned_data.get("endereco")
        if commit:
            user.save()
        return user
    


class UserSocialSignupForm(SocialSignupForm):
    """
    Renders the form when user has signed up using social accounts.
    Default fields will be added automatically.
    See UserSignupForm otherwise.
    """
    




class EspecialidadeForm(forms.ModelForm):
    class Meta:
        model = Especialidade
        fields = ['nome']


class ClinicaForm(forms.ModelForm):
    class Meta:
        model = Clinica
        fields = ['cnpj', 'razao_social', 'nome_fantasia', 'endereco', 'telefone', 'documentos_validacao', 'data_inicio', 'especialidades']


class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['crm', 'nome', 'cpf', 'rg', 'endereco', 'data_nascimento', 'documentos_validacao']


class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['paciente', 'medico', 'clinica', 'data', 'horario', 'agendada']
