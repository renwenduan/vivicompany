# Generated by Django 2.1.4 on 2018-12-26 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gname', models.CharField(max_length=256)),
                ('gprice', models.FloatField()),
                ('gcatalog', models.CharField(max_length=256, null=True)),
                ('gvocation', models.CharField(max_length=256, null=True)),
                ('gshort_details', models.CharField(max_length=2048)),
                ('glong_details', models.CharField(max_length=4056)),
                ('gpub_time', models.TimeField(auto_now=True)),
            ],
        ),
    ]
