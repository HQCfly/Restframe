# Generated by Django 2.1.7 on 2019-03-05 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20190304_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.IntegerField(choices=[(1, '普通用户'), (2, 'VIP'), (3, 'SVIP')], default=1),
        ),
    ]