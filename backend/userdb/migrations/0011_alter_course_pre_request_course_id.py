# Generated by Django 3.2 on 2021-05-17 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userdb', '0010_auto_20210517_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='pre_request_course_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='userdb.course'),
        ),
    ]
