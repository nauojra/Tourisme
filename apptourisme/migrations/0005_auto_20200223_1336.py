# Generated by Django 3.0.3 on 2020-02-23 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptourisme', '0004_auto_20200223_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visite',
            name='telephone',
            field=models.CharField(max_length=10, verbose_name='telephone'),
        ),
    ]