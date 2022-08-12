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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('weight', models.PositiveIntegerField(default=0, null=True)),
                ('shipment_type', models.CharField(choices=[('ground', 'GROUND'), ('air', 'AIR'), ('sea', 'SEA')], max_length=30)),
                ('cost', models.PositiveIntegerField(default=0, help_text='in cents', null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipping', to='order.Order')),
            ],
        ),
        migrations.RemoveField(
            model_name='ground',
            name='order',
        ),
        migrations.RemoveField(
            model_name='sea',
            name='order',
        