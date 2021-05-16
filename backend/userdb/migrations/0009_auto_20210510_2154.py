# Generated by Django 3.2 on 2021-05-10 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdb', '0008_auto_20210510_2148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursedesigner',
            name='id',
        ),
        migrations.RemoveField(
            model_name='lecturer',
            name='id',
        ),
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AddField(
            model_name='coursedesigner',
            name='cd_id',
            field=models.IntegerField(auto_created=True, default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lecturer',
            name='lec_id',
            field=models.IntegerField(auto_created=True, default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='s_id',
            field=models.IntegerField(auto_created=True, default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]