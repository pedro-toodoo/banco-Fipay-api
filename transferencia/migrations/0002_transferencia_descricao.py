# Generated by Django 4.0.2 on 2022-02-07 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transferencia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transferencia',
            name='descricao',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
