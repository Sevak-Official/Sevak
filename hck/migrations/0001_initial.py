# Generated by Django 4.1.1 on 2023-06-27 19:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100, null=True)),
                ('symptoms', models.CharField(choices=[('SELECT', 'SELECT'), ('Discomfort in stomach,Digestive Disorders', 'Discomfort in stomach,Digestive Disorders'), ('Chest Pain', 'Chest Pain'), ('X-Ray', 'X-Ray'), ('Injury,Fracture', 'Injury,Fracture'), ('Problem in Eyes', 'Problem in Eyes'), ('Depression,Mental Health', 'Depression,Mental Health'), ('Skin Problem', 'Skin Problem'), ('Ear,Nose or Throat Issues', 'Ear,Nose or Throat Issues'), ('Kidney Disease', 'Kidney Disease'), ('ToothCheck', 'ToothCheck')], default='SELECT', max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_established', models.DateField(null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('pincode', models.CharField(max_length=6, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('website', models.URLField(null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialization', models.CharField(choices=[('SELECT', 'SELECT'), ('Gastroenterology', 'Gastroenterology(Discomfort in stomach,Digestive Disorders)'), ('Cardiography', 'Cardiography(Chest Pain)'), ('Radiology', 'Radiology(X-Ray)'), ('Orthopedics', 'Orthopedics(Injury,Fracture)'), ('Ophtalmology', 'Ophtalmology(Problem in Eyes)'), ('Psychiatry', 'Psychiatry(Depression,Mental Health)'), ('Dermatology', 'Dermatology(Skin Problem)'), ('Otolaryngologist', 'Otolaryngologist(Ear,Nose or Throat Issues)'), ('Nephrology', 'Nephrology(Kidney Disease)'), ('Dentist', 'Dentist(ToothCheck)')], default='--', max_length=200)),
                ('name', models.CharField(max_length=100)),
                ('clinic_website', models.URLField(null=True)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hck.hospital')),
            ],
        ),
    ]
