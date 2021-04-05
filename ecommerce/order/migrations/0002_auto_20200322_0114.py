# Generated by Django 3.0.3 on 2020-03-22 01:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0001_initial'),
        ('product', '0001_initial'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='air',
            field=models.ForeignKey(db_column='shipping_air', null=True, on_delete=django.db.models.deletion.CASCADE, to='shipping.Air'),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='book',
            field=models.ForeignKey(db_column='product_book', null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Book'),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='e_book',
            field=models.ForeignKey(db_column='product_e_book', null=True, on_delete=django.db.models.deletion.CASCADE, to='product.EBook'),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='ground',
            field=models.ForeignKey(db_column='shipping_ground', null=True, on_delete=django.db.models.deletion.CASCADE, to='shipping.Ground'),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='sea',
            field=models.ForeignKey(db_column='shipping_sea', null=True, on_delete=django.db.models.deletion.CASCADE, to='shipping.Sea'),
        ),
    ]
