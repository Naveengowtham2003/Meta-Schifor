# Generated by Django 5.0.6 on 2024-06-21 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='quantity',
            new_name='quanity',
        ),
    ]
