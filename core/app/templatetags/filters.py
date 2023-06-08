from django import template
register = template.Library()
@register.filter()
def slash_end(string):
    result = ""
    for char in string:
        result += char + "/"
    return result
@register.filter()
def check_length(string):
    if len(string) % 2 == 0:
        return string[:51]+'...'
    elif len(string) % 3 == 0:
        return string[:52]+'...'
    else:
        return string[:50]+'...'
@register.filter()
def add(number,add_number):
    return number + add_number
