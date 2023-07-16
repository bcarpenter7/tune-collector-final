from django import template

register = template.Library()

# use to set a query param, if it exists or not, and without altering other params
# {% load tune_extras %}
# <a href="?{% set_param request 'sort' 'name' %}">
@register.simple_tag
def set_param(request, param, val):
    parameters = request.GET.copy()
    parameters[param] = val
    return parameters.urlencode()
