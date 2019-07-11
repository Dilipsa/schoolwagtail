# Generated by Django 2.2.3 on 2019-07-11 10:02

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('school_name', models.CharField(max_length=200)),
                ('school_address', wagtail.core.fields.RichTextField(null=True)),
            ],
            options={
                'verbose_name': 'about Page',
                'verbose_name_plural': 'about Pages',
            },
            bases=('wagtailcore.page',),
        ),
    ]