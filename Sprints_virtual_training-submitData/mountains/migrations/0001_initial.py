# Generated by Django 4.2.3 on 2023-07-16 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('height', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('fam', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('otc', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Pass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beauty_title', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('other_titles', models.CharField(max_length=255)),
                ('connect', models.TextField(blank=True)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('level', models.JSONField(blank=True, default=dict)),
                ('status', models.CharField(choices=[('new', 'New'), ('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], max_length=255)),
                ('coords', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mountains.coordinate')),
                ('images', models.ManyToManyField(to='mountains.image')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mountains.user')),
            ],
        ),
    ]
