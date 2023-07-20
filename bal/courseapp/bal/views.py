import json
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpRequest, HttpResponse
from bal.forms import UrunForm    #hesap klasörünün altındakı forms.py kategoriyi import ettik
from .models import Urun #burada veri tabnını import ettik
import random #rastgele sayı üretmek için
import os
from django.contrib.auth.decorators import login_required #loginmi kontrolleri için


from django.contrib import messages
import datetime
# Create your views here.





def anasayfa(request):
    return render(request, 'bal/anasayfa.html')

def contact(request):
    return render(request, 'bal/contact.html')

def hakkında(request):
    return render(request, 'bal/hakkında.html')

def shop(request):
    entries = Urun.objects.all()
    return render(request, 'bal/shop.html',{'entries': entries})



def urun_ekle(request):
    if request.method == 'POST':
        form = UrunForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('urun_ekle')  # Yeniden formu temiz bir şekilde göstermek için aynı sayfaya yönlendiriyoruz
    else:
        form = UrunForm()
    return render(request, 'bal/urun_ekle.html', {'form': form})


def urun_detay(request, id, slug): 
    form = get_object_or_404(Urun, id=id)#id bilgisini dışardan gelen
     #idurlsye eşitledik
    return render(request, 'bal/urun_detay.html', {'form': form})



# def home(request):
#     toplam_borc = Ödeme.objects.aggregate(toplam_borc=Sum('miktar'))
#     entries = Ödeme.objects.all()



#     return render(request, 'hesap/hesap.html',{'entries': entries,
#                                                'toplam_borc': toplam_borc, })

# def kartlar(request):
#     entries = Kartlar.objects.all()
#     return render(request, 'hesap/kartlar.html',{'entries': entries})

# def borc(request):
#     toplam_borc = Ödeme.objects.aggregate(toplam_borc=Sum('miktar'))
#     entries = Ödeme.objects.all()


#     return render(request, 'hesap/borc.html',{'entries': entries,
#                                                'toplam_borc': toplam_borc})

# def sonuc(request, id): 
#     data=Kartlar.objects.get(pk=id) #id nosuna göre sorgulama yapar.
#     print(data.isim)
#     if data.isim=="Ziraat":
#         print("gerekli işlemler için seleniuma yönlendirliyorsunuz")
#         ziraat_giris()
#     if data.isim=="Akbank":
#         print("gerekli işlemler için seleniuma yönlendirliyorsunuz")
#         akbank_giris()    
#     if data.isim=="Halkbank":
#         print("gerekli işlemler için seleniuma yönlendirliyorsunuz")
#         halkbank_giris()
#     if data.isim=="Enpara":
#         print("gerekli işlemler için seleniuma yönlendirliyorsunuz")
#         enpara_giris()          

#     return render(request, 'hesap/sonuc.html')

# def gıda(request):
#     harcamalar = gıda.objects.all()
#     return render(request, 'hesap/gıda.html', {'harcamalar': harcamalar})

# def aileharcama(request):
#     toplam_gida_harcamasi = GidaHarcamasi.objects.aggregate(toplam_gida_harcamasi=Sum('tutar'))
#     entries = GidaHarcamasi.objects.all()
#     return render(request, 'hesap/aileharcama.html',{'entries': entries,
#                                                'toplam_gida_harcamasi': toplam_gida_harcamasi,
#                                                })

# def analiz(request):#burada toplam tutarların analizi var

#     entries = Gıdaisimleri.objects.all()

#     if request.method=='POST':
#         ayy=request.POST['ay']
#         yıll=request.POST['yıl']
#         isim=request.POST['gıdaismi']
#         print(f"{ayy}------> {yıll}------->{isim}")
#         toplam = GidaHarcamasi.objects.filter(gida_adi=isim, kayit_tarihi__year=yıll, kayit_tarihi__month=ayy).aggregate(toplam_tutar=Sum('tutar'))
#         print(toplam)
#         return render(request, 'hesap/analiz.html', {'toplam': toplam})#post requesti gelince yönlendirme(anasayfaya yönlendirdi)
#     return render(request, 'hesap/analiz.html',{'entries': entries})







#  #__________________EKLE________________________



# def ekle(request):
#      if request.method == 'POST':
#          form = KategoriForm(request.POST)
#          if form.is_valid():
#              # Form doğrulandı, verileri işle
#              form.save()
#              # Başka bir yere yönlendir
#              return redirect('/')#post requesti gelince yönlendirme(anasayfaya yönlendirdi)
         
#          print(form)
#      else:
#          form = KategoriForm()
#      return render(request, 'hesap/ekle.html', {'form': form})

# def kart_ekle(request):
#      if request.method == 'POST':
#          form = KartForm(request.POST)
#          if form.is_valid():
#              # Form doğrulandı, verileri işle
#              form.save()
#              # Başka bir yere yönlendir
#              return redirect('/kartlar')#post requesti gelince yönlendirme(anasayfaya yönlendirdi)
         
#          print(form)
#      else:
#          form = KartForm()
#      return render(request, 'hesap/kart_ekle.html', {'form': form})

# def eklegıda(request):
#      entries = Gıdaisimleri.objects.all()  
#      if request.method == 'POST':
#          form = GidaHarcamasiForm(request.POST)
#          if form.is_valid():
#              # Form doğrulandı, verileri işle
#              form.save()
#              # Başka bir yere yönlendir
#              return redirect('/aileharcama')#post requesti gelince yönlendirme(anasayfaya yönlendirdi)
         
#          print(form)
#      else:
#          form = GidaHarcamasiForm()
#      return render(request, 'hesap/eklegıda.html', {'form': form,
#                                                     'entries': entries})

# def gıdaisimekle(request):
#     entries = Gıdaisimleri.objects.all()
    
#     if request.method == 'POST':
#         gida_adi = request.POST['gıdaname']
        
#         if Gıdaisimleri.objects.filter(gida_adi=gida_adi).exists():
#             messages.warning(request, 'Bu gıda ismi zaten mevcut.')
#         else:
#             kurslar = Gıdaisimleri(gida_adi=gida_adi)
#             kurslar.save()
#             return redirect('/gıdaisimekle')
    
#     return render(request, 'hesap/gıdaisimekle.html', {'entries': entries})
#     #get requesti gelince yönlendirme





# #__________________SİL________________________
# def kart_sil(request, id): 
#      ödeme = get_object_or_404(Kartlar, id=id)#id bilgisini dışardan gelen
#      #idurlsye eşitledik
#      if request.method == 'POST':
#              ödeme.delete()# Başarılı bir şekilde silme formu yapıldığında yapılacak işlemler
#              return redirect("/kartlar") #anasayfaya yönlendirdi       
            
#      else:
#          form = ödeme
#      return render(request, 'hesap/kart_sil.html', {'form': form})


# def sil(request, id): 
#      ödeme = get_object_or_404(Ödeme, id=id)#id bilgisini dışardan gelen
#      #idurlsye eşitledik
#      if request.method == 'POST':
#              ödeme.delete()# Başarılı bir şekilde silme formu yapıldığında yapılacak işlemler
#              return redirect("/") #anasayfaya yönlendirdi       
            
#      else:
#          form = ödeme
#      return render(request, 'hesap/sil.html', {'form': form})

# def gıda_sil(request, id): 
#      gıdaisim = get_object_or_404(Gıdaisimleri, id=id)#id bilgisini dışardan gelen
#      #idurlsye eşitledik
#      if request.method == 'POST':
#              gıdaisim.delete()# Başarılı bir şekilde silme formu yapıldığında yapılacak işlemler
#              return redirect("/gıdaisimekle") #anasayfaya yönlendirdi       
            
#      else:
#          form = gıdaisim
#      return render(request, 'hesap/gıda_sil.html', {'form': form})

# def silgıdaharcama(request):
#    if request.method=='POST':
#         id_no=request.POST['id_no']
#         ödeme = get_object_or_404(GidaHarcamasi, id=id_no)
#         ödeme.delete()# Başarılı bir şekilde silme formu yapıldığında yapılacak işlemler
#         return redirect("/silgıdaharcama") #anasayfaya yönlendirdi  

#    else:
#         entries = GidaHarcamasi.objects.all()
#         return render(request, 'hesap/silgıdaharcama.html',{'entries': entries})

# def silsercanharcama(request):
#    if request.method=='POST':
#         id_no=request.POST['id_no']
#         ödeme = get_object_or_404(Sercanharcama, id=id_no)
#         ödeme.delete()# Başarılı bir şekilde silme formu yapıldığında yapılacak işlemler
#         return redirect("/silsercanharcama") #anasayfaya yönlendirdi  

#    else:
#         entries = Sercanharcama.objects.all()
#         return render(request, 'hesap/silsercanharcama.html',{'entries': entries})

# def silmehmetharcama(request):
#    if request.method=='POST':
#         id_no=request.POST['id_no']
#         ödeme = get_object_or_404(Mehmetharcama, id=id_no)
#         ödeme.delete()# Başarılı bir şekilde silme formu yapıldığında yapılacak işlemler
#         return redirect("/silmehmetharcama") #anasayfaya yönlendirdi  

#    else:
#         entries = Mehmetharcama.objects.all()
#         return render(request, 'hesap/silmehmetharcama.html',{'entries': entries})

# def silerenharcama(request):
#    if request.method=='POST':
#         id_no=request.POST['id_no']
#         ödeme = get_object_or_404(Erenharcama, id=id_no)
#         ödeme.delete()# Başarılı bir şekilde silme formu yapıldığında yapılacak işlemler
#         return redirect("/silerenharcama") #anasayfaya yönlendirdi  

#    else:
#         entries = Erenharcama.objects.all()
#         return render(request, 'hesap/silerenharcama.html',{'entries': entries})






































# def veritabanı(request):

#     kurslar=Book.objects.all()
#     return render(request,'pages/veritabanı.html',{"kurs":kurslar})

# def index(request):
#     entries = Kategori.objects.all()
#     context = {'entries': entries}

#     return render(request, 'pages/index.html', context)

# def search(request):
#     #burada get sorgusu yaptık.search ile gelen urlde dışarıya results değerini çıkardık
#     query = request.GET.get('q')#get sorgusundan gelen değeri aldık
#     results = Kategori.objects.filter(başlık__contains=query)
#     return render(request, 'pages/search.html', {'results': results})

# def post(request):#EĞER POSTA GİRİLEN DEĞERLERE ŞARTLAR YÜKLEMEK İSTİYORSAK 7.7 DERSİNE BAKILABİLİR
#     if request.method=='POST':
#         imgurl=request.POST['imgurl']
#         başlık=request.POST['başlık']
#         içerik=request.POST['içerik']
#         isActive=request.POST.get("isActive",False)#burada işaretlenmediği zaman hata vermemesinin önüne geçtik
#         if isActive=="on":
#             isActive=True
#         kurslar=Kategori(başlık=başlık,imgurl=imgurl,içerik=içerik,isActive=isActive)    
#         kurslar.save() 
#         return redirect('/pages/index')#post requesti gelince yönlendirme
#     return render(request, 'pages/post.html')#get requesti gelince yönlendirme


# def post2(request):
#     if request.method == 'POST':
#         form = KategoriForm(request.POST)
#         if form.is_valid():
#             # Form doğrulandı, verileri işle
#             form.save()
#             # Başka bir yere yönlendir
#             return redirect("/pages/index")#post requesti gelince yönlendirme
#     else:
#         form = KategoriForm()
#     return render(request, 'pages/post2.html', {'form': form})


# def ürün_detay(request): #güncellemek için
#     entries = Kategori.objects.all()
    
#     return render(request, 'pages/ürün_detay.html',{'entries': entries})




# @login_required(login_url="/account/login") #Login değilse izin verilmez Burada içindeki linke yönlendirdi
# def güncelle(request, idurls):
#     kategori = get_object_or_404(Kategori, id=idurls)#idurls bilgisini dışardan gelen(urls.py.py dosyasından)
#     #idurlsye eşitledik
#     if request.method == 'POST':
#         form = KategoriForm(request.POST, instance=kategori)
#         if form.is_valid(): 
#             form.save()# Başarılı bir şekilde güncellendiğinde yapılacak işlemler
#             return redirect("/pages/ürün_detay")
#     else:
#         form = KategoriForm(instance=kategori)
#     return render(request, 'pages/güncelle.html', {'form': form})



# @login_required(login_url="/account/login") #Login değilse izin verilmez Burada içindeki linke yönlendirdi
# def sil(request, idurls): #burdan devam edilecek
#     kategori = get_object_or_404(Kategori, id=idurls)#id bilgisini dışardan gelen
#     #idurlsye eşitledik
#     if request.method == 'POST':
#             kategori.delete()# Başarılı bir şekilde silme formu yapıldığında yapılacak işlemler
#             return redirect("/pages/ürün_detay")        
            
#     else:
#         form = kategori
#     return render(request, 'pages/sil.html', {'form': form})

# def yükle(request):
#     if request.method == 'POST':
#         imgurl=request.FILES.getlist("dosya")
#         for file in imgurl:
#             dosya_yükleme(file) #dosya yükleme ffonksiyonu ile fotoğraf belirlenen klasöre yüklenir
#         # print(imgurl)#çekilen verinin ismini verir
#         # print(imgurl.name)#çekilen verinin ismini verir
#         # print(imgurl.size)#çekilen boyutunu verir
#         # print(imgurl.content_type)#çekilen verinin türünü verir
        


#         return redirect("/pages/yükle")        
#     return render(request, 'pages/yükle.html')


# def dosya_yükleme(file):
#     number=random.randint(1,99999)#rastgele sayı ürettik
#     filename,file_extention=os.path.splitext(file.name)#file.name verisini uzantı adı ve dosya adına parçaladık
#     name=filename+ "_"+str(number) + file_extention#bunu yeni değişkene atadık
#     with open("temp/"+name,"wb+") as destination: #kızrmızı ile işaretlenen yerler gelen dosyayı belirlenen adrese yazmak için 
#         for chunk in file.chunks():
#             destination.write(chunk)


# def kategori(request):
#     return render(request,'pages/kategori.html')


# def kurslar(request):
#     return HttpResponse("selam pages")


# def anasayfa(request):
#     return HttpResponse("Buda pages anasayfadır")

# def dinamik(request, kategori):
#     return HttpResponse(f"'{kategori}' adlı değişken(int türünde) ile dinamik linke ulaştınız")

# def dinamikstr(request, kategori):
#     return HttpResponse(f"'{kategori}' adlı değişken(str türünde) ile dinamik linke ulaştınız")




# def ziraatt():
#     print("fonksiyon çalıştı")
#     ziraat()#modülü çağırdık