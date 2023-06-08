from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models
from beedoctor.users.managers import UserManager


class User(AbstractUser):
    # Existing fields
    username = models.CharField(_("username"), max_length=150, unique=False, default="")
    email = models.EmailField(_("email address"), unique=True)

    # New fields
    cpf = models.CharField(_("CPF"), max_length=11, blank=True)
    data_nascimento = models.DateField(_("Data de Nascimento"), null=True, blank=True)
    endereco = models.TextField(_("Endereço"), blank=True)

    # Field to store social ID
    social_id = models.CharField(_("Social ID"), max_length=255, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self) -> str:
        # Add implementation of the get_absolute_url method, if needed
        pass

        return reverse("users:detail", kwargs={"pk": self.id})


   




class Especialidade(models.Model):
    OPCOES_ESPECIALIDADE = [
        ("Clínica Geral", "Clínica Geral / Medicina de Família"),
        ("Pediatria", "Pediatria"),
        ("Ginecologia e Obstetrícia", "Ginecologia e Obstetrícia"),
        ("Cardiologia", "Cardiologia"),
        ("Dermatologia", "Dermatologia"),
        ("Ortopedia", "Ortopedia"),
        ("Psiquiatria", "Psiquiatria"),
        ("Oftalmologia", "Oftalmologia"),
        ("Otorrinolaringologia", "Otorrinolaringologia"),
        ("Endocrinologia", "Endocrinologia"),
        ("Gastroenterologia", "Gastroenterologia"),
        ("Neurologia", "Neurologia"),
        ("Urologia", "Urologia"),
        ("Odontologia", "Odontologia"),
        ("Radiologia", "Radiologia"),
        ("Oncologia", "Oncologia"),
        ("Nefrologia", "Nefrologia"),
        ("Reumatologia", "Reumatologia"),
        ("Cirurgia Geral", "Cirurgia Geral"),
    ]
    nome = models.CharField(max_length=100, choices=OPCOES_ESPECIALIDADE)
    

    def __str__(self):
        return self.nome


class Clinica(models.Model):
    cnpj = models.CharField(max_length=18, unique=True)
    razao_social = models.CharField(max_length=100)
    nome_fantasia = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    documentos_validacao = models.FileField(upload_to='documentos/clinicas')
    data_inicio = models.DateField()
    especialidades = models.ManyToManyField(Especialidade)

    def __str__(self):
        return self.nome_fantasia



class Medico(models.Model):
    crm = models.CharField(max_length=20)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    rg = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200)
    data_nascimento = models.DateField()
    documentos_validacao = models.FileField(upload_to='documentos/')
    # Outros campos relacionados ao cadastro do médico

    def __str__(self):
        return self.nome



class Consulta(models.Model):
    paciente = models.ForeignKey(User, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE)
    data = models.DateField()
    horario = models.TimeField()
    agendada = models.BooleanField(default=False)

    def __str__(self):
        return f'Consulta de {self.paciente} com {self.medico}'
