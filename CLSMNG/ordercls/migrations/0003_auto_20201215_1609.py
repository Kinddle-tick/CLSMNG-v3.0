# Generated by Django 3.1.4 on 2020-12-15 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordercls', '0002_auto_20201215_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroomapply',
            name='applyID',
            field=models.IntegerField(auto_created=True, default=0, primary_key=True, serialize=False),
        ),
    ]