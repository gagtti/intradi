# Generated by Django 4.0.3 on 2022-03-22 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.SmallIntegerField()),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre Área')),
            ],
            options={
                'verbose_name': 'Área',
                'verbose_name_plural': 'Áreas',
                'ordering': ['numero'],
            },
        ),
    ]