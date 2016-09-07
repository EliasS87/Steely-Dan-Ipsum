from django.contrib import admin


from . models import Paragraph


class ParagraphAdmin(admin.ModelAdmin):

    list_display = ['created', ]

    class Meta:
        model = Paragraph


admin.site.register(Paragraph, ParagraphAdmin,)
