# Generated by Django 5.1.4 on 2024-12-31 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rsvp',
            old_name='wish',
            new_name='message',
        ),
    ]
