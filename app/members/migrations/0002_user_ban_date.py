# Generated by Django 2.2.9 on 2020-02-09 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ban_date',
            field=models.DateTimeField(null=True),
        ),
    ]
