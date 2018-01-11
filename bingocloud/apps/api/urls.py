from django.conf.urls import patterns, include, url


urlpatterns = patterns('apps.api.views',
    url(r'^run/do.action', 'procedure.run', name = 'api.run'),
 )