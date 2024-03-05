from django import template
register= template.library()

@register.filter(name="hello")
def return_hello(value, arg):
    return "hello !"