from django.db import models

# Create your models here.

class IndexParagraf(models.Model):
    title = models.CharField(("Başlık"), max_length=50)
    header = models.TextField(("Paragraf"))
    text =  models.TextField(("Ana yazı"))
    user = models.CharField(("Kullanıcı Adı"), max_length=50,null=True)
    date_now = models.DateTimeField(("Paylaşım Zamanı"),auto_now_add=True)
    image = models.FileField(("Kullanıcı Profil Fotorafı"), upload_to=None, max_length=100)