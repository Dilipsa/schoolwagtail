# Generated by Django 2.2.3 on 2019-07-11 11:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notificationpage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notificationpage',
            old_name='post',
            new_name='carrier_post',
        ),
        migrations.RemoveField(
            model_name='notificationpage',
            name='numbers',
        ),
        migrations.AddField(
            model_name='notificationpage',
            name='carrier_subject',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='notificationpage',
            name='required',
            field=models.IntegerField(default=0),
        ),
    ]
