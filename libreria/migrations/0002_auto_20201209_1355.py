# Generated by Django 3.1.3 on 2020-12-09 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autore_lf',
            options={'verbose_name': 'autore', 'verbose_name_plural': 'autori'},
        ),
        migrations.AlterModelOptions(
            name='genere_lf',
            options={'verbose_name': 'genere', 'verbose_name_plural': 'generi'},
        ),
        migrations.AlterModelOptions(
            name='libro_lf',
            options={'verbose_name': 'libro', 'verbose_name_plural': 'libri'},
        ),
    ]