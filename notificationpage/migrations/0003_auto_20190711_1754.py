# Generated by Django 2.2.3 on 2019-07-11 12:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notificationpage', '0002_auto_20190711_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificationpage',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='notificationpage',
            name='event',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notificationpage',
            name='exam_for',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notificationpage',
            name='fro',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='notificationpage',
            name='to',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='notificationpage',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]