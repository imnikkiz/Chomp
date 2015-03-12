from django.conf.urls import patterns, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'search.views.home_page', name='home'),

    url(r'^register_form/$', 'search.views.register_form', name='register_form'),
    url(r'^register/$', 'search.views.register', name='register'),

    url(r'^login_form/$', 'search.views.login_form', name='login_form'),
    url(r'^login_user/$', 'search.views.login_user', name='login_user'),

    url(r'^logout/$', 'search.views.logout_user', name='logout'),


    url(r'^recipe_main$', 'search.views.recipe_main', name='recipe_main'),
    
    url(r'^search_page/$', 'search.views.search_page', name='search_page'),
    url(r'^new_search/$', 'search.views.new_search', name='new_search'),

    url(r'^recipe/(?P<recipe_id>\d+)/$', 'search.views.recipe_details', name='recipe_details'),
    url(r'^remove_recipes/$', 'search.views.remove_recipes', name='remove_recipes'),    
    url(r'^add_recipe/$', 'search.views.add_recipe', name='add_recipe'),
    url(r'^my_recipes/$', 'search.views.my_recipes', name='my_recipes'),
    
    url(r'^add_to_planner/$', 'search.views.add_to_planner', name='planner'),
    url(r'^planner/$', 'search.views.planner', name='planner'),
    url(r'^update_planner/$', 'search.views.update_planner', name='update_planner'),


    url(r'^clear_planner/$', 'search.views.clear_planner', name='clear_planner'),
    url(r'^shopping_list/$', 'search.views.shopping_list', name='shopping_list'),

    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
)
