# Generated by Django 2.0.1 on 2018-02-01 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='thumb_image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=''),
        ),
    ]
