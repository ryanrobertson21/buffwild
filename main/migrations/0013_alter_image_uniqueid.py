# Generated by Django 3.2.3 on 2022-05-25 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_image_img_url_image_tradeid_alter_image_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='uniqueId',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
