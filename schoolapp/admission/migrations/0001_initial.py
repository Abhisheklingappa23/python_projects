# Generated by Django 3.2.5 on 2021-09-02 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('father', models.CharField(max_length=1000)),
                ('class_name', models.IntegerField()),
                ('contact', models.CharField(max_length=1000)),
            ],
        ),
    ]
