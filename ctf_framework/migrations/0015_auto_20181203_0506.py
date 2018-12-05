# Generated by Django 2.0.1 on 2018-12-03 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('ctf_framework', '0014_remove_challenge_point_value'),
    ]

    operations = [
        migrations.RenameModel('ChallengeCategory', 'Category'),
        migrations.RenameField('Category', 'category', 'name'),
        migrations.AlterField(
            model_name='challenge',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ctf_framework.Category'),
        )
    ]