# Generated by Django 4.2.1 on 2023-06-12 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0001_june_1_2023_johnconnor_api'),
        ('voyage', '0005_remove_voyagesourcesconnection_zotero_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='broadregion',
            name='geo_location',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='geo.location', verbose_name='New Location Fieldmapping'),
        ),
        migrations.AlterField(
            model_name='place',
            name='geo_location',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='geo.location', verbose_name='New Location Fieldmapping'),
        ),
        migrations.AlterField(
            model_name='region',
            name='geo_location',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='geo.location', verbose_name='New Location Fieldmapping'),
        ),
    ]
