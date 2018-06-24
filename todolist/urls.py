from django.conf.urls import url, include
from .views import Login, GetLists, ListDetails, GetTasks, TaskDetails, GetUsers, Logout, ListDelete, TaskDelete,\
    Registration, Activate, ShareGetTasks, ShareTaskDetails

urlpatterns = [
    url(r'^login/$', Login),
    url(r'^login/registr/$', Registration),
    url(r'^getlists/$', GetLists),
    url(r'^getlists/(?P<list_id>[0-9]+)/$', ListDetails),
    url(r'^getlists/(?P<list_id>[0-9]+)/delete/$', ListDelete),
    url(r'^getlists/(?P<list_id>[0-9]+)/gettasks/$', GetTasks),
    url(r'^getlists/(?P<list_id>[0-9]+)/sharegettasks/$', ShareGetTasks),
    url(r'^getlists/(?P<list_id>[0-9]+)/gettasks/(?P<task_id>[0-9]+)/$', TaskDetails),
    url(r'^getlists/(?P<list_id>[0-9]+)/sharegettasks/(?P<task_id>[0-9]+)/$', ShareTaskDetails),
    url(r'^getlists/(?P<list_id>[0-9]+)/gettasks/(?P<task_id>[0-9]+)/delete/$', TaskDelete),
    url(r'^getlists/getusers/$', GetUsers),
    url(r'^logout/$', Logout),
    url(r'^activate/(?P<activation_key>[\w-]+)/$', Activate),
]