# Generated by Django 3.0.3 on 2020-03-09 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.PositiveIntegerField(help_text='in cents')),
                ('weight', models.PositiveIntegerField(help_text='in grams')),
            ],
            options={
                'abstract': Fal