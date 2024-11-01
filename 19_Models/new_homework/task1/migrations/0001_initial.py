# Generated by Django 4.2.16 on 2024-11-01 05:46

from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('balance', models.TextField(verbose_name=django.db.models.fields.DecimalField)),
                ('age', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('cost', models.TextField(verbose_name=django.db.models.fields.DecimalField)),
                ('size', models.TextField(verbose_name=django.db.models.fields.DecimalField)),
                ('description', models.TextField()),
                ('age_limited', models.BooleanField(verbose_name=False)),
                ('DecimalField', models.IntegerField()),
                ('BooleanField', models.BooleanField()),
                ('buyer', models.ManyToManyField(related_name='courses', to='task1.buyer')),
            ],
        ),
    ]
