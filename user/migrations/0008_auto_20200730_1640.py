# Generated by Django 3.0.8 on 2020-07-30 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20200729_1750'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userskintrouble',
            name='skinTrouble',
        ),
        migrations.RemoveField(
            model_name='userskintrouble',
            name='user',
        ),
        migrations.RemoveField(
            model_name='user',
            name='skinTrouble',
        ),
        migrations.AddField(
            model_name='user',
            name='skinTrouble',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.DeleteModel(
            name='SkinTrouble',
        ),
        migrations.DeleteModel(
            name='UserSkinTrouble',
        ),
    ]
