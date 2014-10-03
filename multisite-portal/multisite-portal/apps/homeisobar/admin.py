from apps.common.admin import ItemSlugAdmin
from apps.multilingual.admin import admin
from apps.homeisobar.models import Home
from django.contrib import admin
from django.core.urlresolvers import reverse
from apps.common import utils
from apps.common.encode import Encode
import settings
from django.contrib import messages
from multilingual.utils import GLL
from apps.multilingual.admin import MultilingualModelAdmin,MultilingualInlineAdmin


class HomeAdmin(MultilingualModelAdmin):
    list_display = ('title',)
    
    search_fields = ['title']
    
    use_fieldsets = (
        ('Featured', {
            'fields': ('featured_case_studies','featured_news_1'),
        }),
        ('Content', {
            'fields': ('active', 'title', 'headline',),
        }),
        ('Metadata', {
           'fields': ('meta_description',)
        }),          
    )

    
    filter_horizontal = ('featured_case_studies',)
    
admin.site.register(Home, HomeAdmin)