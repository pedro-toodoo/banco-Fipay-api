# Generated by Django 4.0.1 on 2022-02-04 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deposito', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposito',
            name='saldo',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]