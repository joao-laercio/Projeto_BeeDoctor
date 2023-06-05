from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.forms import EmailField
from django.utils.translation import gettext_lazy as _
from django import forms
from .models import Especialidade, Clinica, Medico, Consulta
User = get_user_model()


class UserAdminChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User
        field_classes = {"email": EmailField}


class UserAdminCreationForm(admin_forms.UserCreationForm):
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    class Meta(admin_forms.UserCreationForm.Meta):
        model = User
        fields = ("email",)
        field_classes = {"email": EmailField}
        error_messages = {
            "email": {"unique": _("This email has already been taken.")},
        }


class UserSignupForm(SignupForm):
    """
    Form that will be rendered on a user sign up section/screen.
    Default fields will be added automatically.
    Check UserSocialSignupForm for accounts created from social.
    """


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
