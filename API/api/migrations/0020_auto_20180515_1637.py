# Generated by Django 2.0.5 on 2018-05-15 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20180515_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='check',
            field=models.BooleanField(default=False),
        ),
    ]
