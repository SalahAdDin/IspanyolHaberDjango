from django import template

register = template.Library()



#@register.filter(name='substring')
@register.filter
def search(value, arg):
	import re

	return re.search(arg, value).group()


@register.filter
def sub(value, arg):
	import re

	return re.sub(arg,
		'',
		value)
