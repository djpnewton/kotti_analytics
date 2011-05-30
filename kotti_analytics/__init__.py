from pyramid.renderers import render

from kotti.util import extract_from_settings
from kotti.views.slots import register
from kotti.views.slots import RenderRightSlot
from kotti.views.slots import RenderLeftSlot

ANALYTICS_WIDGET_DEFAULTS = {
    'tracking_id': '',
    }

def render_analytics_widget(context, request, name=''):
    prefix = 'kotti_analytics.'
    if name:
        prefix += name + '.'
    variables = ANALYTICS_WIDGET_DEFAULTS.copy()
    variables.update(extract_from_settings(prefix))
    return render('templates/analytics_widget.pt', variables)

def include_widget(config, where=RenderRightSlot):
    register(where, None, render_analytics_widget)

def include_widget_left(config):
    include_widget(config, RenderLeftSlot)
