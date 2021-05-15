# Generated by Django 3.2.3 on 2021-05-15 15:24

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vessels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('code', models.CharField(max_length=100, unique=True, verbose_name='code')),
                ('location', models.CharField(max_length=100, verbose_name='location')),
                ('status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive'), ('under_maintenance', 'under_maintenance')], default='active', max_length=20)),
                ('vessel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vessels.vessel', verbose_name='vessel')),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'abstract': False,
            },
        ),
    ]