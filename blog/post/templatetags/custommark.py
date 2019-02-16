from  django import template
import markdown
register = template.Library()

@register.filter
def mark(value):
    return markdown.markdown(value)


