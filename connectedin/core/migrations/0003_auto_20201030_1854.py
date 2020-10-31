# Generated by Django 3.1 on 2020-10-30 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200926_0215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='status',
            field=models.CharField(choices=[('accepted', 'Accepted'), ('rejected', 'Rejected'), ('waiting', 'Waiting')], default='waiting', max_length=10),
        ),
    ]