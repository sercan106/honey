from bal.models import Urun

def urun(request): 
    veri =  Urun.objects.all()
    return {
        'ürün': veri
    }