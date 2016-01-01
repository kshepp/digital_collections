from django.conf.urls import url

from . import views

urlpatterns = [
	# /main_colleciton
	url(r'^$', views.index, name='index'),
	# /main_collection/collections/
	
# url for collections isn't working
	url(r'^collection/(?P<location>[a-z0-9\-]+)/$', views.collections, name='collection'),
	url(r'^collection/?$', views.collections, name='collection'),
	# /main_collection/items/
	url(r'^item/(?P<location>[a-z0-9\-]+)/$', views.item_specific, name='item'),
	url(r'^item/?$', views.all_items, name='all_items'),
	# /main_collection/exhibits/
	url(r'^exhibit/(?P<location>[a-z0-9\-]+)/$', views.exhibit, name='exhibit'),
	url(r'^exhibits/?$', views.all_exhibits, name='all_exhibits'),
	#Edit button
	url(r'^edit/(?P<item_id>[0-9]+)/$', views.edit_item, name="edit_item")

]
