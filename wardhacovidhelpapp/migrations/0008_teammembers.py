# Generated by Django 3.2 on 2021-05-13 04:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wardhacovidhelpapp', '0007_auto_20210509_1922'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, null=True)),
                ('Profession', models.CharField(max_length=200, null=True)),
                ('Title', models.TextField(max_length=500, null=True)),
                ('ProfileImage', models.ImageField(upload_to='static/img')),
                ('JoiningDate', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
