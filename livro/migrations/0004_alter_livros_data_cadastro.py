# Generated by Django 4.0.2 on 2022-02-22 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0003_alter_livros_options_alter_livros_co_autor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='data_cadastro',
            field=models.DateField(auto_now=True),
        ),
    ]
