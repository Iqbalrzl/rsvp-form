# Generated by Django 5.1.4 on 2024-12-31 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0003_alter_rsvp_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsvp',
            name='message',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
