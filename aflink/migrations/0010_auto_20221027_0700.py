# Generated by Django 3.2.15 on 2022-10-27 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aflink', '0009_auto_20221025_0657'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_requested', models.CharField(max_length=100, verbose_name='Material Requested')),
                ('Description', models.TextField()),
                ('quantity', models.IntegerField()),
                ('width', models.DecimalField(decimal_places=0, max_digits=10)),
                ('height', models.DecimalField(decimal_places=0, max_digits=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='jobcard',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='jobcard',
            name='name',
        ),
        migrations.RemoveField(
            model_name='jobcard',
            name='sortno',
        ),
        migrations.AddField(
            model_name='jobcard',
            name='contact',
            field=models.CharField(max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='jobcard',
            name='customer',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='jobcard',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='jobcard',
            name='job_descritpion',
            field=models.TextField(null=True, verbose_name='Job Description'),
        ),
        migrations.AddField(
            model_name='jobcard',
            name='job_type',
            field=models.CharField(max_length=50, null=True, verbose_name='Job Type'),
        ),
        migrations.AddField(
            model_name='jobcard',
            name='order_number',
            field=models.CharField(max_length=50, null=True, verbose_name='Order Number'),
        ),
    ]
