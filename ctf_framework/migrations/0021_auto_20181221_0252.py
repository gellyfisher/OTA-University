# Generated by Django 2.0.1 on 2018-12-21 02:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ctf_framework', '0020_auto_20181205_0226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ctf_framework.UserProfile'),
        ),
    ]