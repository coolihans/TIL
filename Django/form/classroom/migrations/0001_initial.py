# Generated by Django 3.2.12 on 2022-04-07 01:25

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
                ('name', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=20)),
                ('is_cs', models.BooleanField()),
                ('age', models.IntegerField()),
            ],
        ),
    ]