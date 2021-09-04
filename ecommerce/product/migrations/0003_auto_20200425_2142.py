# Generated by Django 3.0.3 on 2020-04-25 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_delete_orderdetail'),
        ('product', '0002_auto_20200322_0126'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='order',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='order.Order'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ebook',
            name='order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ebooks', to='order.Order'),
            preserve_default=False,
        ),
    ]
