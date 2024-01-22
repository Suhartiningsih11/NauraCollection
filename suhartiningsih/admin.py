from django.contrib import admin
from .models import Kategori, Produk, Slide, Kontak,Profil,Statis, ChatID

class KategoriAdmin(admin.ModelAdmin):
    list_display = ("nama", "aktif","banner_satu","banner_dua",)
    prepopulated_fields = {"slug": ("nama",)}
    
class ProdukAdmin(admin.ModelAdmin):
    list_display = ("nama_produk", "gambar_satu","no_whatsup", "diskon","harga", "keterangan_barang",)
    prepopulated_fields = {"slug": ("nama_produk",)}

#DIBENERIN DULU KAYAK DIATAS
# class DataSlideAdmin(admin.ModelAdmin):
#     list_display = ("teks_awal", "teks_dua","aktif","gambar_slide",)
#     prepopulated_fields = {"slug": ("gambar_slide",)}
    
# class DataKontakAdmin(admin.ModelAdmin):
#     list_display = ("nama", "no_whatsup","email","subject",)
#     prepopulated_fields = {"slug": ("nama",)}
    
# class DataProfilAdmin(admin.ModelAdmin):
#     list_display = ("nama_produk", "gambar","diskon","keterangan_barang",)
#     prepopulated_fields = {"slug": ("nama_produk",)}

class StatisAdmin(admin.ModelAdmin):
    list_display = ("email", "telepon","alamat_kami",)
    prepopulated_fields = {"slug": ("email",)}
    
admin.site.register(Kategori, KategoriAdmin)
admin.site.register(Produk, ProdukAdmin)
admin.site.register(Slide)
admin.site.register(Kontak)
admin.site.register(Profil)
admin.site.register(Statis)
admin.site.register(ChatID)

