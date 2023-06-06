from django.contrib.auth import get_user_model
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from .serializers import MedicosSerializer,ClinicaSerializer,ConsultaSerializer,EspecialidadeSerializer
from .serializers import UserSerializer
from beedoctor.users.models import Medico,Clinica,Consulta,Especialidade


User = get_user_model()


class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "pk"

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False)
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)

class MedicosViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicosSerializer


class ClinicaViewSet(viewsets.ModelViewSet):
    serializer_class = ClinicaSerializer
    queryset = Clinica.objects.all()

class ConsultaViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ConsultaSerializer
    queryset = Consulta.objects.all()
    
class EspecialidadeViewSet(viewsets.ModelViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer


class RealizarConsultaViewSet(viewsets.ModelViewSet):
    serializer_class = ConsultaSerializer
    queryset = Consulta.objects.all()
    http_method_names = ['post']  # Limita a viewset ao método POST
    permission_classes = []  # Define as permissões necessárias para acessar a viewset
    authentication_classes = []  #