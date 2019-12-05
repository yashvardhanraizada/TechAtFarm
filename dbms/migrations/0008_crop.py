# Generated by Django 2.2.2 on 2019-06-25 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbms', '0007_auto_20190624_1802'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crop_name', models.CharField(max_length=100)),
                ('moisture', models.IntegerField(default=0)),
                ('threshold', models.IntegerField(default=0)),
                ('recommendation', models.TextField(default='')),
            ],
        ),
    ]