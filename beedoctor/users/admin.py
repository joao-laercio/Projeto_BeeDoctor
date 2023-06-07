from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.forms import UsernameField
from django.utils.translation import gettext_lazy as _

from beedoctor.users.forms import UserSignupForm

from .models import Medico, Clinica, Consulta,Especialidade
   


User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserSignupForm
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("user", "cpf", "data_nascimento", "endereco", "username")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["email", "get_user", "cpf", "data_nascimento", "endereco", "username"]
    search_fields = ["email", "user", "username"]
    ordering = ["id"]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "username"),
            },
        ),
    )

    def get_user(self, obj):
        return obj.username

    get_user.short_description = _("User")
    
    
    
    
 



class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = ['nome']



class ClinicaAdmin(admin.ModelAdmin):
    list_display = ['nome_fantasia', 'cnpj', 'endereco', 'telefone', 'data_inicio']
    filter_horizontal = ['especialidades']



class MedicoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'crm', 'cpf', 'rg', 'endereco', 'data_nascimento']



class ConsultaAdmin(admin.ModelAdmin):
    list_display = ['paciente', 'medico', 'clinica', 'data', 'horario', 'agendada']

    
    
    
admin.site.register(Medico,MedicoAdmin)
admin.site.register(Clinica,ClinicaAdmin)
admin.site.register(Consulta,ConsultaAdmin)
admin.site.register(Especialidade,EspecialidadeAdmin)
