# Generated by Django 3.0.3 on 2020-02-23 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptourisme', '0003_auto_20200223_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='lienHotel',
            field=models.CharField(blank=True, max_length=300, verbose_name=" lien de l'hotel"),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='lienRestaurant',
            field=models.CharField(max_length=300, verbose_name=' lien du restaurant'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='noteRestaurant',
            field=models.FloatField(verbose_name='note du restaurant'),
        ),
    ]