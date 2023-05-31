import ast

from django import template
from slider.models import SliderItem

register = template.Library()


@register.inclusion_tag('slider.html')
def render_slider_items(page, tags: str):
    tags_list = ast.literal_eval(tags)
    slider_items = SliderItem.objects.filter(page=page, tags__name__in=tags_list)
    return {'slider_items': slider_items}
