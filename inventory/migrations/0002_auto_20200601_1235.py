# Generated by Django 3.0.6 on 2020-06-01 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desktop',
            name='status',
            field=models.CharField(choices=[('AVAILABLE', 'Item available for purchase'), ('SOLD', 'Item not currently available'), ('RESTOCKING', 'Item will be availble in few days - restocking')], default='SOLD', max_length=10),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='status',
            field=models.CharField(choices=[('AVAILABLE', 'Item available for purchase'), ('SOLD', 'Item not currently available'), ('RESTOCKING', 'Item will be availble in few days - restocking')], default='SOLD', max_length=10),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='status',
            field=models.CharField(choices=[('AVAILABLE', 'Item available for purchase'), ('SOLD', 'Item not currently available'), ('RESTOCKING', 'Item will be availble in few days - restocking')], default='SOLD', max_length=10),
        ),
    ]
