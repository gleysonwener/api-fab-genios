from django.contrib import admin
from.models import Pedido, ItemDoPedido
from cliente.models import Cliente
from produto.models import Produto

#admin.site.register(Pedido)
#admin.site.register(ItemDoPedido)
admin.site.register(Cliente)
admin.site.register(Produto)

class ItensInLine(admin.TabularInline):
    model = ItemDoPedido

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    inlines = (ItensInLine,)