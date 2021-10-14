from django.urls import re_path

from .views import DocumentsByTagViewSet


app_name = 'app'


urlpatterns = [
    re_path(r'^document/(?P<topic>\w+)/(?P<folder>\w+)/$',
            DocumentsByTagViewSet.as_view()),
    re_path(r'^document/(?P<topic>.+)/$',
            DocumentsByTagViewSet.as_view(), name='topic')
]
