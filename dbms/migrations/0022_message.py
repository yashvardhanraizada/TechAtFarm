# Generated by Django 2.2.2 on 2019-06-28 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbms', '0021_auto_20190627_1112'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('mobile_number', models.CharField(max_length=10)),
                ('subject', models.CharField(max_length=30)),
                ('message', models.CharField(max_length=200)),
            ],
        ),
    ]
