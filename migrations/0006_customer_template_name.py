# Generated by Django 2.0.5 on 2019-03-20 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0005_auto_20190320_0406'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='template_name',
            field=models.CharField(default='NULL', editable=False, max_length=100),
        ),
    ]
