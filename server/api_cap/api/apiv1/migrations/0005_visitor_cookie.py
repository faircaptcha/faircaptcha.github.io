# Generated by Django 3.1.7 on 2021-04-21 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiv1', '0004_auto_20210417_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='cookie',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
