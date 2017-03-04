from django.conf.urls import include, url
from store import urls
from django.contrib import admin
from store import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'bookstore.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('store.urls'), name='store'),
    url(r'accounts/',include('registration.backends.default.urls')),

]
