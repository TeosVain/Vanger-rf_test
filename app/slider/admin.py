from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminMixin
from easy_thumbnails.files import get_thumbnailer

from .models import SliderItem


@admin.register(SliderItem)
class SliderItemAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("order", "preview", "title", "is_active")
    list_display_links = ("preview", "title")
    list_editable = ("is_active",)
    list_filter = ("is_active",)
    search_fields = ("title",)
    ordering = ("order", "id")
    fieldsets = (
        (None, {"fields": ("title", "image", "is_active", "order")}),
        ("Предпросмотр", {"fields": ("preview",)}),
    )
    readonly_fields = ("preview",)

    @admin.display(description="Миниатюра")
    def preview(self, obj):
        if not obj or not obj.image:
            return "—"
        thumbnailer = get_thumbnailer(obj.image.file)
        thumb = thumbnailer.get_thumbnail({"size": (120, 80), "crop": True})
        return format_html(
            '<img src="{}" alt="{}" style="width:120px;height:80px;object-fit:cover;border-radius:8px;" />',
            thumb.url,
            obj.title,
        )


admin.site.site_header = "Администрирование слайдера"
admin.site.site_title = "Админка"
admin.site.index_title = "Управление контентом"
