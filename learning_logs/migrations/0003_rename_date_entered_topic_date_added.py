# Generated by Django 4.2.6 on 2023-10-24 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("learning_logs", "0002_entry"),
    ]

    operations = [
        migrations.RenameField(
            model_name="topic", old_name="date_entered", new_name="date_added",
        ),
    ]
