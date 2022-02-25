from rest_framework import serializers, pagination

from .models import Hobby, Persona, Reunion


class HobbySerializer(serializers.ModelSerializer):

    class Meta:
        model = Hobby
        fields = (
            'id',
            'hobby'
        )


class PersonaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Persona
        fields = '__all__'


class PersonaSerializer4(serializers.ModelSerializer):
    """ Many to many """
    estado = serializers.BooleanField(default=False)
    hobbies = HobbySerializer(many=True)
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Persona
        fields = (
            'id',
            'primer_nombre',
            'segundo_nombre',
            'primer_apellido',
            'segundo_apellido',
            'full_name',
            'trabajo',
            'correo',
            'celular',
            'estado',
            'hobbies',
        )

    def get_full_name(self, obj):
        if obj.segundo_nombre and obj.segundo_apellido:
            return f'{obj.primer_nombre} {obj.segundo_nombre} {obj.primer_apellido} {obj.segundo_apellido}'
        elif obj.segundo_nombre:
            return f'{obj.primer_nombre} {obj.segundo_nombre} {obj.primer_apellido}'
        elif obj.segundo_apellido:
            return f'{obj.primer_nombre} {obj.primer_apellido} {obj.segundo_apellido}'


class PersonaPagination(pagination.PageNumberPagination):
    page_size = 50  # Bloques
    max_page_size = 200  # En memoria

# ForeignKey


class ReunionSerializer(serializers.ModelSerializer):

    persona = PersonaSerializer4()

    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'persona',
        )


class ReunionSerializerLink(serializers.HyperlinkedModelSerializer):

    persona = PersonaSerializer4()
    
    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'persona',
        )
        extra_kwargs = {
            'persona': {
                'view_name': 'app_persona:api_detalle_personas',
                'lookup_field': 'pk'
            }
        }
        
class CountReunionSerializer(serializers.Serializer):
    persona__trabajo = serializers.CharField()
    cantidad = serializers.IntegerField()
