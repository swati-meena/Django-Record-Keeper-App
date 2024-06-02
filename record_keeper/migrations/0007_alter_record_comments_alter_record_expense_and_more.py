# Generated by Django 5.0.2 on 2024-03-08 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record_keeper', '0006_alter_record_activity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='comments',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='record',
            name='expense',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Expense ($)'),
        ),
        migrations.AlterField(
            model_name='record',
            name='hours',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='record',
            name='mileage',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='record',
            name='travel',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='record',
            name='wait',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=4),
        ),
    ]
