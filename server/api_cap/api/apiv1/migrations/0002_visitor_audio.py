# Generated by Django 3.1.7 on 2021-04-10 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiv1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='audio',
            field=models.FileField(null=True, upload_to='./captcha_img/'),
        ),
    ]
