# Generated by Django 2.1.7 on 2019-04-12 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giftcards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giftcard',
            name='barcode',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]