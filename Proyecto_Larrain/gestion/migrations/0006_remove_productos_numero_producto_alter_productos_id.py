# Generated by Django 5.0.6 on 2024-07-01 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0005_productos_numero_producto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productos',
            name='numero_producto',
        ),
        migrations.AlterField(
            model_name='productos',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
