# Generated by Django 2.0.1 on 2018-02-07 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctf_framework', '0005_userprofile_is_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='url',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
