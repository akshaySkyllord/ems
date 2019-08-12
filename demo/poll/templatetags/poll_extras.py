from django import template
from poll.models import Question


register = template.Library()

def upper(value, n):
    """Converts a string into all uppercase"""
    return value.upper()[0:n]

register.filter('upper', upper)

@register.simple_tag()
def recent_poll(n=5, **kwargs):
    questions = Question.objects.all().order_by('-created_at')
    return questions






