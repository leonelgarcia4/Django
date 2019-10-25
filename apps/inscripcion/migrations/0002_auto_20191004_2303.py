# Generated by Django 2.2.6 on 2019-10-05 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscripcion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='dias',
            fields=[
                ('nombre', models.CharField(max_length=15, primary_key=True, serialize=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='horario',
            name='dias',
        ),
        migrations.AddField(
            model_name='horario',
            name='dias',
            field=models.ManyToManyField(to='inscripcion.dias'),
        ),
    ]