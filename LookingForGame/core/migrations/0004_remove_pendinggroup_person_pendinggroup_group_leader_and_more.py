# Generated by Django 4.0.3 on 2022-05-14 20:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_alter_group_group_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pendinggroup',
            name='person',
        ),
        migrations.AddField(
            model_name='pendinggroup',
            name='group_leader',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='leader', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pendinggroup',
            name='pending_group_id',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pendinggroup',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='group',
            name='age_minimum',
            field=models.CharField(choices=[('any', 'Any age'), ('13+', '13+'), ('18+', '18+')], default='18+', max_length=20),
        ),
        migrations.AlterField(
            model_name='group',
            name='experience_level',
            field=models.CharField(choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')], default='Intermediate', max_length=20),
        ),
        migrations.AlterField(
            model_name='group',
            name='group_size',
            field=models.CharField(choices=[('2-3', '2-3'), ('4-6', '4-6'), ('7+', '7+')], default='5', max_length=20),
        ),
        migrations.AlterField(
            model_name='group',
            name='meeting_frequencies',
            field=models.CharField(choices=[('twice weekly', 'Twice Weekly'), ('weekly', 'Weekly'), ('twice monthly', 'Twice Monthly'), ('montly', 'Monthly'), ('other', 'Other')], default='Weekly', max_length=20),
        ),
        migrations.AlterField(
            model_name='pendinggroup',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orig_group_number', to='core.group'),
        ),
    ]
