# Generated by Django 3.2.9 on 2021-11-09 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frase', models.TextField()),
                ('autor', models.CharField(max_length=150)),
                ('tags', models.ManyToManyField(blank=True, related_name='quotes', to='quotes.Tag')),
            ],
        ),
    ]
