from django import template

register = template.Library()


@register.inclusion_tag('slider.html')
def render_templatetags(images):
    return {'images': images}
