# Generated by Django 3.2.5 on 2021-11-07 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reciept', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='corespondintReciept',
            new_name='reciept',
        ),
    ]