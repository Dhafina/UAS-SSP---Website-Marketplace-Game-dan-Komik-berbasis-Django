# Generated by Django 5.0.3 on 2024-07-10 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kodebrg', models.CharField(max_length=8)),
                ('nama', models.CharField(max_length=50)),
                ('stok', models.IntegerField()),
                ('harga', models.BigIntegerField()),
                ('link_gbr', models.CharField(blank=True, max_length=150)),
            ],
        ),
    ]
