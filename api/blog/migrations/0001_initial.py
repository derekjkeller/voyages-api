# Generated by Django 4.2.1 on 2023-10-21 15:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import filebrowser.fields
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('description', models.CharField(blank=True, max_length=600, null=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('intro', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('description', models.CharField(blank=True, max_length=600, null=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('role', models.CharField(max_length=200)),
                ('photo', filebrowser.fields.FileBrowseField(blank=True, max_length=300, null=True, verbose_name='Thumbnail')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='institution_authors', to='blog.institution')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('language', models.CharField(choices=[('de', 'German'), ('en', 'English'), ('es', 'Spanish'), ('pt-br', 'Portuguese')], default='en', max_length=5, null=True)),
                ('subtitle', models.CharField(blank=True, max_length=200, null=True)),
                ('slug', models.SlugField(max_length=200)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('content', tinymce.models.HTMLField()),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('thumbnail', filebrowser.fields.FileBrowseField(blank=True, max_length=300, verbose_name='Thumbnail')),
                ('authors', models.ManyToManyField(related_name='posts', to='blog.author')),
                ('tags', models.ManyToManyField(to='blog.tag')),
            ],
            options={
                'ordering': ['-created_on'],
                'unique_together': {('slug', 'language')},
            },
        ),
    ]
