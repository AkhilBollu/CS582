# Generated by Django 2.0.7 on 2018-07-02 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0003_auto_20180702_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='summary',
            field=models.TextField(),
        ),
    ]
