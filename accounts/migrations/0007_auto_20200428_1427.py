# Generated by Django 3.0.4 on 2020-04-28 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200428_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='is_employable',
            field=models.TextField(default='false'),
        ),
    ]
