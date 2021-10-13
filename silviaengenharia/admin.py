from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import PaginaCliente, Cliente, Email, MensagemParaTodos

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')
    list_filter = ('email',)
    list_per_page = 10

class EmailAdmin(SummernoteModelAdmin):
    summernote_fields = ('mensagem',)

class MensagemParaTodosAdmin(SummernoteModelAdmin):
    summernote_fields = ('mensagem', )

admin.site.register(PaginaCliente)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Email, EmailAdmin)
admin.site.register(MensagemParaTodos, MensagemParaTodosAdmin)