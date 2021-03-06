# Generated by Django 3.1.5 on 2021-02-13 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time when the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time when the object was last modified.', verbose_name='modified at')),
                ('name', models.TextField(blank=True, max_length=500)),
                ('serial_number', models.TextField(blank=True, max_length=500)),
                ('model', models.TextField(blank=True, max_length=500)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('price', models.FloatField()),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MachineType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time when the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time when the object was last modified.', verbose_name='modified at')),
                ('name', models.TextField(blank=True, max_length=500)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MachineFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time when the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time when the object was last modified.', verbose_name='modified at')),
                ('name', models.TextField(blank=True, max_length=500)),
                ('path', models.TextField(blank=True, max_length=500)),
                ('file', models.FileField(blank=True, null=True, upload_to='machines/files/', verbose_name='Machine Quote')),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='machines.machine')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='machine',
            name='machine_type',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='machines.machinetype'),
        ),
    ]
