# Generated by Django 3.1.4 on 2020-12-15 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordercls', '0004_auto_20201215_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroomapply',
            name='status',
            field=models.CharField(choices=[(0, '批准'), (1, '未受理'), (2, '拒绝')], default='未受理', max_length=30),
        ),
    ]