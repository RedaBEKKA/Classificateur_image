# Generated by Django 2.2 on 2020-07-05 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to=None)),
                ('classified', models.CharField(blank=True, max_length=100)),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
