# Generated by Django 4.2.6 on 2024-03-19 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('caption', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='addmoney_info',
            name='Category',
            field=models.CharField(choices=[('Food', 'Food'), ('Travel', 'Travel'), ('Shopping', 'Shopping'), ('Necessities', 'Necessities'), ('Entertainment', 'Entertainment'), ('Games', 'Games'), ('Books', 'Books'), ('Other', 'Other')], default='Food', max_length=20),
        ),
    ]