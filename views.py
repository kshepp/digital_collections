from django.shortcuts import render_to_response, render, get_object_or_404
from django.template import Context, loader
from django.template import RequestContext

# Create your views here.
from django.http import HttpResponse
from .models import Item, Collection, Exhibit

def index(request):
	entries = Collection.objects.all()
	collections = Collection.objects.all()
	Context = {'entries': entries,'collections': collections}
	return render(request, 'main_collection/main_collection.html', Context)

#collection isn't working
def collections(request,location):
	collection = Collection.objects.get(location=location)
	items = Item.objects.filter(collections__location=location)
	Context = {'items': items,'collection': collection}
	return render(request, 'main_collection/collection.html', Context)

def item(request, location):
	entries = Item.objects.filter(location=location)
	Context = {'entries': entries}
	return render(request,'main_collection/item.html', Context)

def item_specific(request, location):
	entries = Item.objects.filter(location=location)
	Context = {'entries': entries}
	return render(request,'main_collection/item_specific.html', Context)

def all_items(request):
	entries = Item.objects.all()
	Context = {'entries': entries}
	return render(request,'main_collection/item.html', Context)

def exhibit(request, location):
	exhibit = Exhibit.objects.get(location=location)
	items = Item.objects.filter(exhibit__location="gallery")
	Context = {'exhibit': exhibit, 'items': items}

	if exhibit.get_layout_display()=="Text":
		return render(request,'main_collection/exhibit_text.html', Context)

	elif exhibit.get_layout_display()=="Text and Image":
		return render(request, 'main_collection/exhibit_text_image.html', Context)
	
	elif exhibit.get_layout_display()=="Gallery":
		return render(request, 'main_collection/exhibit_gallery.html', Context)

	elif exhibit.get_layout_display()=="Map":
		return render(request, 'main_collection/exhibit_map.html', Context)
	
	else:
		return HttpResponse(exhibit.get_layout_display())

def all_exhibits(request):
	entries = Exhibit.objects.all()
	Context = {'entries': entries}
	return render(request,'main_collection/all_exhibits.html', Context)

def edit_item(request, location):
	entries = Item.objects.filter(location=location)
	Context = {'entries': entries}
	return render(request,'main_collection/edit_item.html', Context)


