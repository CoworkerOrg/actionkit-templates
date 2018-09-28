import json
from actionkit_app.contexts.event_context_json import event_json
from actionkit_app.contexts.contexts_loader import contexts
from django.http import HttpResponse
from django.shortcuts import render
from actionkit_app.contexts.contexts_loader import contexts

def homepage_index(request):
  ctx = {
        'page': {'title':'Homepage'},
        'pagelinks': sorted(contexts.items())
        }

  return render(request, 'renderer_homepage.html', ctx)

def template_index(request, name, page):
  print "name: " + name
  print "page: " + page
  context_data = contexts.get(name,{})
  ctx = dict()
  # TODO: Review this and other MO functions
  if page:
    context_data = contexts.get(name, {}).get(page, {})
  ctx.update(context_data)
  return render(request, page, ctx)

def login_context(request):
    event_json_copy = event_json.copy()
    coming_from = request.GET.get('url','')
    if 'event' in coming_from \
       or 'logged_in' in coming_from \
       or 'survey_logged_in' in coming_from:
        if not request.GET.get('login') and 'survey_logged_in' not in coming_from:
            del event_json_copy['name']
        # TODO: Use render() instead
        # TODO: Figure out how to toggle logged in or not with ?login=1; this endpoint is hit but does not return the correct context
        return HttpResponse(
            'actionkit.forms.onContextLoaded(%s)' % json.dumps(event_json_copy))
    else:
        return HttpResponse(
            #text key has all the generic error messages
            'actionkit.forms.onContextLoaded({"text": %s})' % json.dumps(event_json['text']))
