from django.conf import settings as settings_conf
from django import template

template.add_to_builtins('apps.common.templatetags.page')
template.add_to_builtins('apps.footer.templatetags.footer')
template.add_to_builtins('apps.social.templatetags.social')

def settings(request):
    return {
        'settings': settings_conf
    }