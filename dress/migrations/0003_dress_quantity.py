# Generated by Django 2.0.7 on 2020-12-29 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dress', '0002_auto_20201229_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='dress',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]