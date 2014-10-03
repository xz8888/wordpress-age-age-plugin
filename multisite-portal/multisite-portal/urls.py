from django.conf import settings
#from django.conf.urls.defaults import *
from apps.transurlvania.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template
from apps.news.feeds import NewsFeed

admin.autodiscover()

urlpatterns = lang_prefixed_patterns('' ,
	(r'^tinymce/', include('apps.tinymce.urls')),
	
	url(r'^people/$', 'people.views.index', name='people_view'),
	url(r'^people/person/(?P<person>[a-zA-Z0-9-_]+)/$', 'people.views.person', name='person_view'),
	url(r'^people/person/(?P<person>[a-zA-Z0-9-_]+).ajax$', 'people.views.person', {'ajax': True}, name='person_ajax_view'),
	url(r'^people/(?P<page>[0-9]+)/$', 'people.views.people_page', name='people_page_view'),
	url(r'^people/(?P<page>[0-9x]+)/([0-9y]{1}).ajax', 'people.views.people_page', {'ajax': True}, name='people_page_ajax_view'),
	
	url(r'^people/department/(?P<slug>[a-zA-Z0-9-_]+)/$', 'people.views.department_page', name='people_department_view'),
	url(r'^people/department/(?P<slug>[a-zA-Z0-9-_]+)/(?P<page>[0-9]+)/$', 'people.views.department_page', name='people_department_page_view'),
	url(r'^people/department/(?P<department>[a-zA-Z0-9-_]+)/person/(?P<person>[a-zA-Z0-9-_]+)/$', 'people.views.person_department', name='people_department_person_view'),
	url(r'^people/department/(?P<department>[a-zA-Z0-9-_]+)/person/(?P<person>[a-zA-Z0-9-_]+).ajax$', 'people.views.person_department', {'ajax': True}, name='people_department_person_ajax_view'),
	url(r'^people/department/(?P<slug>[a-zA-Z0-9-_]+)/(?P<page>[0-9x]+)/([0-9y]{1}).ajax', 'people.views.department_page', {'ajax': True}, name='department_ajax_view'),
	
	url(r'^work/(?P<slug>[a-zA-Z0-9-_]+)/$', 'work.views.casestudy', name="work_view"),
	url(r'^work/(?P<slug>[a-zA-Z0-9-_]+).ajax$', 'work.views.casestudy', {'ajax': True}, name="work_view_ajax"),
	url(r'^work/$', 'work.views.index', name="works_view"),
	
	url(r'^join/(?P<slug>[a-zA-Z0-9-_]+)/$', 'jobs.views.job', name="job_view"),
	url(r'^join/$', 'jobs.views.index', name="jobs_view"),
	
	url(r'^news/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[a-zA-Z0-9-_]+)/$', 'news.views.story', name="news_story_view"),
	url(r'^news/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$', 'news.views.archive_day', name="news_archive_day_view"),
	url(r'^news/(?P<year>\d{4})/(?P<month>\d{1,2})/$', 'news.views.archive_month', name="news_archive_month_view"),
	url(r'^news/(?P<year>\d{4})/$', 'news.views.archive_year', name="news_archive_year_view"),
	url(r'^news/archive/$', 'news.views.archive', name="news_archive_view"),
	url(r'^news/categories/(?P<slug>[a-zA-Z0-9-_]+)/(?P<page>[0-9]+).ajax$', 'news.views.category_page', {'ajax': True}, name="news_category_page_view"),
	url(r'^news/categories/(?P<slug>[a-zA-Z0-9-_]+)/(?P<page>[0-9]+)/$', 'news.views.category_page', name="news_category_page_view"),
	url(r'^news/categories/(?P<slug>[a-zA-Z0-9-_]+)/$', 'news.views.category', name="news_category_view"),
	
	
	url(r'^news/(?P<page>[0-9]+)/$', 'news.views.news_page', name='news_page_view'),
	url(r'^news/(?P<page>[0-9]+).ajax$', 'news.views.news_page', {'ajax': True}, name='news_page_ajax_view'),
	url(r'^news/archive/$', 'news.views.archive', name="news_archive_view"),
	url(r'^news/$', 'news.views.index', name="news_view"),
	url(r'^news/rss/$', NewsFeed(), name='news_rss'),
	
	url(r'^about/$', 'about.views.index', name='about_view'),

	url(r'^isobar-network/$', direct_to_template, {'template': 'isobar_network.html'}),

	url(r'^social/share.ajax', 'social.views.share', name="share_view"),

	url(r'^receive-casestudy/$', 'apps.work.views.recieve_casestudy', name='receive_casestudy_view'),
	url(r'^receive-newsstory/$', 'apps.news.views.recieve_newsstory', name='receive_newsstory_view'),
	url(r'^receive-relatedlinks/$', 'apps.news.views.recieve_relatedlinks', name='recieve_relatedlinks_view'),
	
	url(r'^contact/$', 'contact.views.index', name='contact_view'),

	url(r'^$', 'home.views.index', name="home_view"),
)
urlpatterns += patterns('',
    url(r'^$', 'home.views.index', name="home_view"),
    (r'^admin/', include(admin.site.urls)),
    (r'^admin/filebrowser/', include('apps.filebrowser.urls')),
    
    (r'^i18n/', include('django.conf.urls.i18n')),
)
					


if settings.DEV_MODE:
	urlpatterns += patterns('',
		(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)