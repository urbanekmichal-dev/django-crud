# Generated by Django 4.1.3 on 2022-12-28 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
    ]
