# Generated by Django 3.0.3 on 2020-05-05 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_delete_orderdetail'),
        ('shipping', '0003_auto_20200425_2142'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipping',
            fields=[
    