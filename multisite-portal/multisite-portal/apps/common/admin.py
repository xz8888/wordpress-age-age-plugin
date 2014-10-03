from apps.multilingual.admin import MultilingualModelAdmin

class ItemAdmin(MultilingualModelAdmin):
	exclude = ['subclass']
	
	
class ItemSlugAdmin(ItemAdmin):
	prepopulated_fields = {'slug': ('title', )}

	