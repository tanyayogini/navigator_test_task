# Generated by Django 4.2.5 on 2023-09-07 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0004_alter_shop_options_alter_shop_city_alter_shop_close_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shop',
            old_name='close_uts',
            new_name='close_utc',
        ),
    ]
