# Generated by Django 4.2.5 on 2023-09-28 13:10

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BloodGroup',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('blood_group', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'blood_group',
                'verbose_name_plural': 'blood_groups',
                'db_table': 'crud_blood_group',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='BloodData',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('mobile_number', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.TextField()),
                ('willing_to_donate', models.BooleanField(default=False)),
                ('profile_pic', models.ImageField(upload_to='profile')),
                ('blood_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.bloodgroup')),
            ],
            options={
                'verbose_name': 'blood_data',
                'verbose_name_plural': 'blood_datas',
                'db_table': 'crud_blood_data',
                'ordering': ('-created_at',),
            },
        ),
    ]
