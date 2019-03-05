from django import template

register = template.Library()

@register.filter(name='split')
def split(value, arg):
	return value.split('%20')

@register.filter(name='rem')
def rem(value):
	if value[:7] == '/media/':
		return value[7:]
	else:
		return value