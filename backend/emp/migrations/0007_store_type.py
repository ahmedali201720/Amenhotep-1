# Generated by Django 3.0.6 on 2020-06-24 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0006_store_tower'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='Type',
            field=models.CharField(choices=[('gym', 'Gym'), ('restaurant', 'Restaurant'), ('cafe', 'Cafe'), ('shop', 'Shop')], default='shop', max_length=12),
        ),
    ]