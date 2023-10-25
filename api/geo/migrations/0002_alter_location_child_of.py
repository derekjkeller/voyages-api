# Generated by Django 4.2.1 on 2023-10-25 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='child_of',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='geo.location', verbose_name='Child of'),
        ),
    ]
