# Generated by Django 2.1.7 on 2019-04-12 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('giftcards', '0003_auto_20190412_1959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='image',
        ),
    ]
