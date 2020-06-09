from django.contrib import admin
from bill.models import Client, Produit, Facture, LigneFacture
from bill.models import Fournisseur


admin.site.register(Client)
admin.site.register(Facture)
admin.site.register(Produit)
admin.site.register(LigneFacture)
admin.site.register(Fournisseur)

