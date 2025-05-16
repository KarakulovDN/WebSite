from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='resize_image')
def resize_image(image_field, size):
    """
    Фильтр для изменения размера изображения
    Использование: {{ product.image|resize_image:"300x200" }}
    """
    if not image_field:
        return ""

    width, height = size.split('x')
    return mark_safe(
        f'<img src="{image_field.url}" '
        f'style="max-width: {width}px; max-height: {height}px;" '
        f'alt="Изображение товара">'
    )
