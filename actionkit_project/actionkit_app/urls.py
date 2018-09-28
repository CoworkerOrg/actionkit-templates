from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^actionkit/$', 'actionkit_app.views.homepage_index'),
    url(r'^context', 'actionkit_app.views.login_context'),
    url(r'^(?P<name>[-.\w]+)?(/(?P<page>[-.\w]+))?$', 'actionkit_app.views.template_index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
