# Generated by Django 2.1.2 on 2019-02-01 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_featureimages'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeatureImagesTwo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
