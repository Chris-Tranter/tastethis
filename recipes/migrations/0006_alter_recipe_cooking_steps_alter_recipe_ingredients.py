# Generated by Django 4.2.13 on 2024-07-22 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cooking_steps',
            field=models.TextField(max_length=1200, unique=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(max_length=600, unique=True),
        ),
    ]
