from django.conf.urls import patterns, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'search.views.home_page', name='home'),
    url(r'^register/$', 'search.views.register', name='register'),
    url(r'^login/$', 'search.views.login_user', name='login'),
    url(r'^recipe_main$', 'search.views.recipe_main', name='recipe_main'),
    url(r'^search_page$', 'search.views.search_page', name='search'),
    url(r'^recipe/(?P<recipe_id>\d+)/$', 'search.views.recipe_details', name='recipe_details'),
    url(r'^my_recipes/$', 'search.views.my_recipes', name='my_recipes'),
    url(r'^planner/$', 'search.views.planner', name='planner'),
    url(r'^shopping_list/$', 'search.views.shopping_list', name='shopping_list'),
    url(r'^results_page$', 'search.views.results_page', name='results'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
)
