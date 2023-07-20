from django.db import models
import datetime
from django.utils.text import slugify #slugify (java-kursu) import ettik


class Urun(models.Model):
    ad = models.CharField(max_length=100)
    aciklama = models.TextField()
    fiyat = models.DecimalField(max_digits=10, decimal_places=2)
    resim = models.ImageField(upload_to='bal_resmi/')

    kayit_tarihi = models.DateField(auto_now_add=True)
    isActive=models.BooleanField()
    slug=models.SlugField(default="", null=False, blank=True)# boş geçilebilir null=False ile

    def __str__(self):
        return self.ad

    def save(self,*args, **kwargs):
        self.slug=slugify(self.ad) #slug işlemleri için sonradan oluşturuldu isimden slug yapıyor
        super().save(args,kwargs)







