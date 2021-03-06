# Generated by Django 2.2.2 on 2019-06-24 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbms', '0004_auto_20190623_0856'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogger_name', models.CharField(max_length=100)),
                ('blogger_description', models.CharField(max_length=200)),
                ('blog_heading', models.CharField(max_length=50)),
                ('blog_description', models.CharField(max_length=200)),
                ('blog_data', models.CharField(max_length=5000)),
            ],
        ),
    ]
