# Generated by Django 5.0 on 2024-04-06 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_logindetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='file',
            field=models.FileField(default='TEST', upload_to='public/'),
            preserve_default=False,
        ),
    ]
