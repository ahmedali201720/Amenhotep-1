# Generated by Django 3.0.6 on 2020-06-25 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0010_auto_20200625_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='Code',
            field=models.IntegerField(),
        ),
    ]
