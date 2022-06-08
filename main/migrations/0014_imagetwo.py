# Generated by Django 4.0.2 on 2022-06-01 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_image_uniqueid'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageTwo',
            fields=[
                ('id', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('ownerWallet', models.CharField(default='Locked', max_length=200)),
                ('uniqueId', models.IntegerField(blank=True, null=True)),
                ('tradeId', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
                ('img_photo', models.ImageField(blank=True, null=True, upload_to='unlocked_buffs/')),
                ('img_url', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
