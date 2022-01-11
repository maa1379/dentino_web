# Generated by Django 3.1.6 on 2022-01-11 07:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clinic', '0019_clinic_notification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Winner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expertise', models.CharField(max_length=150)),
                ('created', models.DateField(auto_now_add=True)),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.clinic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]