from django.contrib import admin

# Register your models here.
from exemplo.forms import PessoaFormAdmin
from exemplo.models import Pessoa


class PessoaAdmin(admin.ModelAdmin):
    form = PessoaFormAdmin

    class Media:
        js= (
            "jquery.mask.min.js",
            "custom.js"
        )

admin.site.register(Pessoa, PessoaAdmin)
