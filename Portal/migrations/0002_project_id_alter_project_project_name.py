# Generated by Django 4.1.9 on 2024-07-10 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
