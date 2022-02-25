from django.db import models
from model_utils.models import TimeStampedModel
from .managers import ReunionManager
# Create your models here.


class Hobby(TimeStampedModel):
    """ Modelo para registrar hobbies de una persona """

    hobby = models.CharField(
        'Pasa tiempo', max_length=50)

    class Meta:
        verbose_name = 'Hobby'
        verbose_name_plural = 'Hobbies'

    def __str__(self):
        return self.hobby


class Persona(TimeStampedModel):
    """ Modelo para registrar peronas de una agenda """

    primer_nombre = models.CharField(
        'Primer Nombre', max_length=50, blank=False, null=False)
    segundo_nombre = models.CharField(
        'Segundo Nombre', max_length=50, blank=True, null=True)
    primer_apellido = models.CharField(
        'Primer Apellido', max_length=50, blank=False, null=False)
    segundo_apellido = models.CharField(
        'Segundo Apellido', max_length=50, blank=True, null=True)
    full_name = models.CharField(
        'Nombre Completo', max_length=100, blank=True, null=True)
    trabajo = models.CharField('Trabajo', max_length=30, blank=True, null=True)
    correo = models.EmailField('Correo', blank=True, null=True)
    celular = models.CharField('Celular', max_length=20, blank=True, null=True)
    hobbies = models.ManyToManyField(Hobby)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

    def __str__(self):
        return self.primer_nombre


class Reunion(TimeStampedModel):
    """ Modelo para reuniones """

    persona = models.ForeignKey(
        Persona,
        on_delete=models.CASCADE
    )
    fecha = models.DateField()
    hora = models.TimeField()
    asunto = models.CharField(
        'Asunto', max_length=100)

    objects = ReunionManager()
    
    class Meta:
        verbose_name = 'Reunion'
        verbose_name_plural = 'Reuniones'

    def __str__(self):
        return self.asunto
