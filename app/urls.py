
from  django61501.urls import url
from    app  import views
urlpatterns= [
    #url(r'^table',views.table),
     url(r'^login/$', views.login,name='login'),
     url(r'^$',views.index),
     url(r'^register/$',views.register,name='register'),
     url(r'^apply1/$',views.apply1,),
    #url(r'add_publisher',views.add_publisher)
    url(r'^add_publisher1/$',views.add_publisher1,name='add_publisher1',),
    url(r'^add_publisher2/$',views.add_publisher2,name='add_publisher2',),
    url(r'^add_publisher$',views.add_publisher,name='add_publisher',),
    #url(r'^yanzheng/$',views.yanzheng,name='yanzheng'),
    url(r'^reg$',views.register,name = 'reg'),
    url(r'^test$',views.test,name = 'test'), #和html  <form method='post' action="{url 'test'}">
    # url(r'^test$',direct_to_templates{tempalte,'login.html'}),
    url(r'^time/$',views.current_datetime),
    url(r'^userlist/$',views.userlist),
    url(r'^insert/$',views.insert_user),
    url(r'^home/$', views.home, name= 'cliente_home'),
    url(r'^show_user/', views.show_user, name='user_list'),
    url(r'^create_user/',views.create_user,name='user_create'),
    url(r'^user_del/(?P<pk>\d)/',views.user_del,name='user_del'),
    url(r'^user_update/(?P<pk>\d)$',views.user_update,name='user_update'),
    # url(r'^cliente_create1/$', views.cliente_create1, name= 'cliente_create'),
    # url(r'^cliente/(?P<pk>\d+)', views.cliente_update,name='cliente_update'),
]
