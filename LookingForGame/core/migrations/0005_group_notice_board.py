# Generated by Django 4.0.3 on 2022-05-14 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_pendinggroup_person_pendinggroup_group_leader_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='notice_board',
            field=models.CharField(default='This is the default notice board message. Use this space to discuss scheduling and other important information!', max_length=240),
        ),
    ]