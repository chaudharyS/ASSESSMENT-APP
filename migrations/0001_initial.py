# Generated by Django 2.0.5 on 2019-03-15 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('employee_count', models.IntegerField()),
            ],
        ),
    ]