from django.views.generic import TemplateView
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    RetrieveDestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
)

from .models import Persona, Reunion
from .serializers import (
    PersonaPagination,
    PersonaSerializer,
    PersonaSerializer4,
    ReunionSerializer,
    ReunionSerializerLink,
    CountReunionSerializer
)

# Create your views here.


class PersonaTemplateView(TemplateView):
    template_name = 'persona/lista.html'


class PersonListApiView(ListAPIView):
    serializer_class = PersonaSerializer
    pagination_class = PersonaPagination

    def get_queryset(self):
        return Persona.objects.all()


class PersonListApiViewFilter(ListAPIView):
    serializer_class = PersonaSerializer

    def get_queryset(self):
        kword = self.kwargs['kword']
        return Persona.objects.filter(
            full_name__icontains=kword
        )


class PersonCreateAPIView(CreateAPIView):
    serializer_class = PersonaSerializer


class PersonDetailAPIView(RetrieveAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer4


class PersonDeleteAPIView(DestroyAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer


class PersonRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer


class PersonUpdateAPIView(UpdateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer


class PersonRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer


# Test modificando el serializador
class PersonaApiList(ListAPIView):
    serializer_class = PersonaSerializer4

    def get_queryset(self):
        return Persona.objects.all()


class ReunionListAPIView(ListAPIView):
    serializer_class = ReunionSerializer

    def get_queryset(self):
        return Reunion.objects.all()


class ReunionListAPIViewLink(ListAPIView):
    serializer_class = ReunionSerializerLink

    def get_queryset(self):
        return Reunion.objects.all()

class ReunionByPersonJOb(ListAPIView):
    serializer_class = CountReunionSerializer
    pagination_class = PersonaPagination

    def get_queryset(self):
        return Reunion.objects.cantidad_reuniones_job()