# Generated by Django 4.0.2 on 2022-02-08 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_operations_operation_alter_operation_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricehistory',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='main.product', verbose_name='Product'),
        ),
    ]
