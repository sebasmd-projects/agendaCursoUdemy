# Generated by Django 3.2.12 on 2022-02-25 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0002_auto_20220224_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='full_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombre Completo'),
        ),
    ]