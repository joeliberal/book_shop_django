# Generated by Django 3.1.7 on 2021-03-05 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_bookinstance_borrower'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_read_private_section', 'VIP User'), ('user_watcher', 'User Watcher'))},
        ),
    ]
