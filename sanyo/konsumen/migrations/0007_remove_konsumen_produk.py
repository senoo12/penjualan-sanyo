# Generated by Django 4.0.6 on 2022-09-20 01:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('konsumen', '0006_alter_konsumen_produk'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='konsumen',
            name='produk',
        ),
    ]
