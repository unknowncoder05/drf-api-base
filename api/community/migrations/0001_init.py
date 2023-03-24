# Generated by Django 3.2 on 2021-10-16 23:25

import api.community.models.reaction
from django.db import migrations, models
import django.db.models.deletion
import django_enum_choices.choice_builders
import django_enum_choices.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='updated at')),
                ('deleted_at', models.DateTimeField(help_text='Date time on which the object was deleted.', null=True, verbose_name='deleted at')),
                ('content', models.CharField(max_length=300)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'get_latest_by': 'created_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='updated at')),
                ('deleted_at', models.DateTimeField(help_text='Date time on which the object was deleted.', null=True, verbose_name='deleted at')),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'get_latest_by': 'created_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='updated at')),
                ('deleted_at', models.DateTimeField(help_text='Date time on which the object was deleted.', null=True, verbose_name='deleted at')),
                ('description', models.CharField(max_length=30)),
                ('url', models.URLField(max_length=60)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'get_latest_by': 'created_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='updated at')),
                ('deleted_at', models.DateTimeField(help_text='Date time on which the object was deleted.', null=True, verbose_name='deleted at')),
                ('type', django_enum_choices.fields.EnumChoiceField(blank=True, choice_builder=django_enum_choices.choice_builders.value_value, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], enum_class=api.community.models.reaction.ReactionTypes, max_length=1, null=True)),
                ('comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reactions', to='community.comment')),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'get_latest_by': 'created_at',
                'abstract': False,
            },
        ),
    ]