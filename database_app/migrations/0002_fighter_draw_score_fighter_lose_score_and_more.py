# Generated by Django 5.0.7 on 2024-07-27 14:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fighter',
            name='draw_score',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinLengthValidator(0)]),
        ),
        migrations.AddField(
            model_name='fighter',
            name='lose_score',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinLengthValidator(0)]),
        ),
        migrations.AddField(
            model_name='fighter',
            name='win_score',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinLengthValidator(0)]),
        ),
        migrations.AlterField(
            model_name='fighter',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
