# Generated by Django 2.0.5 on 2018-05-16 11:14

from django.db import migrations, models
import rest_framework.compat


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_template_fk_template'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='check',
            field=models.IntegerField(default=0, validators=[rest_framework.compat.MinValueValidator(0), rest_framework.compat.MaxValueValidator(1)]),
        ),
    ]
