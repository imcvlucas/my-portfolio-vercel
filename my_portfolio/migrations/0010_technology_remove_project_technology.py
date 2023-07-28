# Generated by Django 4.0.6 on 2022-10-01 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_portfolio', '0009_project_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'technology',
                'verbose_name_plural': 'technologies',
                'ordering': ('name',),
            },
        ),
        migrations.RemoveField(
            model_name='project',
            name='technology',
        ),
    ]
