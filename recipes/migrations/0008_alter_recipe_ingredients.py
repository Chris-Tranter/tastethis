# Generated by Django 4.2.13 on 2024-07-23 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_alter_recipe_cooking_steps_alter_recipe_ingredients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(max_length=3200, unique=True),
        ),
    ]
