# Generated by Django 5.0.2 on 2024-03-02 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record_keeper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='date',
            field=models.DateField(blank=True),
        ),
    ]