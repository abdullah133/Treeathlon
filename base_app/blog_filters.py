from django import template
register = template.Library()
import settings

@register.filter('read_more')
def read_more(body, absolute_url):
	if '<!--more-->' in body:
		return body[:body.find('<!--more-->')]+'<a href="'+str(absolute_url)+'">'+str(settings.READ_MORE_TEXT)+'</a>'
	else:
		return body
