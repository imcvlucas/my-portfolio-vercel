# Generated by Django 4.0.6 on 2022-09-30 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_portfolio', '0005_project_in_progress_alter_project_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(db_index=True, max_length=400),
        ),
    ]
