from django import template
from services.utils import get_annonces

register =template.Library()

@register.simple_tag()
def annonce_tags(request):
    return get_annonces(request)