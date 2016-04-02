from django import template


register = template.Library()


@register.filter
def tagify(value):
    from tags.utils import get_tagify_content
    return get_tagify_content(value)