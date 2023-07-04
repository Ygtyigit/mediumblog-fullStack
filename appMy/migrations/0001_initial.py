# Generated by Django 4.1.3 on 2023-06-19 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IndexParagraf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Başlık')),
                ('header', models.TextField(verbose_name='Paragraf')),
                ('text', models.TextField(verbose_name='Ana yazı')),
                ('user', models.CharField(max_length=50, null=True, verbose_name='Kullanıcı Adı')),
                ('date_now', models.DateTimeField(auto_now_add=True, verbose_name='Paylaşım Zamanı')),
                ('image', models.FileField(upload_to=None, verbose_name='Kullanıcı Profil Fotorafı')),
            ],
        ),
    ]