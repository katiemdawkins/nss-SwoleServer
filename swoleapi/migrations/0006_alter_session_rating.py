# Generated by Django 4.0.5 on 2022-06-10 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swoleapi', '0005_session_is_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='rating',
            field=models.IntegerField(default=1),
        ),
    ]
