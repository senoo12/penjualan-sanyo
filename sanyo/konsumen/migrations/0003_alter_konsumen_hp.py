# Generated by Django 4.0.6 on 2022-09-20 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('konsumen', '0002_alter_produk_jasa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='konsumen',
            name='hp',
            field=models.IntegerField(),
        ),
    ]