# Generated by Django 4.0.6 on 2022-10-09 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_portfolio', '0011_alter_project_programming_languages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='live_url',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
    ]
