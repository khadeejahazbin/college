# Generated by Django 4.1.7 on 2023-03-19 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField()),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='department')),
            ],
            options={
                'verbose_name': 'department',
                'verbose_name_plural': 'departments',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('DOB', models.DateField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=50)),
                ('phone_no', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=250)),
                ('department', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=50)),
                ('purpose', models.CharField(max_length=50)),
                ('material_provide', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'orders',
                'ordering': ('first_name',),
            },
        ),
    ]
