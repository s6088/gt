# Generated by Django 2.2.4 on 2019-09-29 11:11

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
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identity_no', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('joining_date', models.DateField(blank=True, null=True)),
                ('license_category', models.CharField(blank=True, choices=[('high', 'Created'), ('medium', 'Medium'), ('low', 'Low')], default='low', max_length=50, null=True)),
                ('license_expire', models.DateField(blank=True, null=True)),
                ('phone_no', models.CharField(blank=True, max_length=100, null=True)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=20)),
                ('created_by', models.ForeignKey(blank=True, default=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Helper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identity_no', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('joining_date', models.DateField(blank=True, null=True)),
                ('phone_no', models.CharField(blank=True, max_length=100, null=True)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=20)),
                ('created_by', models.ForeignKey(blank=True, default=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('driver_salary', models.DecimalField(decimal_places=2, max_digits=20)),
                ('helper_salary', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('driver_lunch_cost', models.DecimalField(decimal_places=2, max_digits=20)),
                ('helper_lunch_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('driver_dinner_cost', models.DecimalField(decimal_places=2, max_digits=20)),
                ('helper_dinner_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('driver_allowance', models.DecimalField(decimal_places=2, max_digits=20)),
                ('helper_allowance', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('created_by', models.ForeignKey(blank=True, default=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_maker', models.CharField(blank=True, max_length=100, null=True)),
                ('engine_no', models.CharField(blank=True, max_length=100, null=True)),
                ('body_making_date', models.DateField(blank=True, null=True)),
                ('purchase_date', models.DateField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('registration_date', models.DateField(blank=True, null=True)),
                ('registration_no', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.CharField(blank=True, max_length=100, null=True)),
                ('created_by', models.ForeignKey(blank=True, default=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='entries.Driver')),
                ('helper', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='entries.Helper')),
                ('vehicle_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entries.VehicleType')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('service_type', models.CharField(blank=True, choices=[('date', 'Date'), ('km', 'KM'), ('both', 'Both')], default='date', max_length=50, null=True)),
                ('created_by', models.ForeignKey(blank=True, default=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicing_date', models.DateTimeField(blank=True, null=True)),
                ('expire_date', models.DateTimeField(blank=True, null=True)),
                ('expire_km', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('workshop', models.CharField(blank=True, max_length=100, null=True)),
                ('service_charge', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('created_by', models.ForeignKey(blank=True, default=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('service_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entries.ServiceName')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entries.Vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
                ('departure_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField()),
                ('starting_km', models.DecimalField(decimal_places=2, max_digits=20)),
                ('ending_km', models.DecimalField(decimal_places=2, max_digits=20)),
                ('user', models.CharField(blank=True, max_length=100, null=True)),
                ('started_from', models.CharField(blank=True, max_length=100, null=True)),
                ('destination', models.CharField(blank=True, max_length=100, null=True)),
                ('octane_expense', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('petrol_expense', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('cng_expense', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('created_by', models.ForeignKey(blank=True, default=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entries.Driver')),
                ('helper', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='entries.Helper')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entries.Vehicle')),
            ],
        ),
        migrations.AddField(
            model_name='helper',
            name='vehicle_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='entries.VehicleType'),
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expense_date', models.DateTimeField(blank=True, null=True)),
                ('purpose', models.CharField(max_length=100)),
                ('memo_no', models.CharField(blank=True, max_length=100, null=True)),
                ('remark', models.CharField(blank=True, max_length=100, null=True)),
                ('total_ammount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('expected_ammount', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('created_by', models.ForeignKey(blank=True, default=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entries.Post')),
            ],
        ),
        migrations.AddField(
            model_name='driver',
            name='vehicle_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='entries.VehicleType'),
        ),
    ]
