from django.conf.urls import patterns, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'search.views.home_page', name='home'),
    url(r'^recipe/(?P<recipe_id>\d+)/$', 'search.views.recipe_details', name='recipe_details'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
)
