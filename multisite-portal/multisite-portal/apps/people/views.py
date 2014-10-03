from apps.people.models import Department, Person
from django import template
from django.conf import settings
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
import random

template.add_to_builtins('apps.people.templatetags.people')

def index(request):
	if settings.ISOBAR_SITE_BOOL:
		return people_page(
				request,
				1,
				len(Person.objects.all().filter(layoutitem_ptr__item_ptr__active=True)
			)
		)
	else:
		return people_page(request, 1)

def person(request, person, ajax = False):
	person = _get_person(person)

	parent_template = 'base.html'
	if ajax:
		parent_template = 'blank.html'

	return render_to_response('person.html', {
			'person': person,
			'parent_template': parent_template,
			'ajax': ajax,
		}, context_instance=RequestContext(request)
	)

def person_department(request, department, person, ajax=False):
	person = _get_person(person)
	department = Department.objects.all() \
			.filter(item_ptr__active=True).get(slug=department)

	parent_template = 'base.html'
	if ajax:
		parent_template = 'blank.html'

	return render_to_response('person.html', {
			'person': person,
			'department': department,
			'ajax': ajax,
			'parent_template': parent_template,
		}, context_instance=RequestContext(request)
	)

def _get_person(person):
	try:
		person = Person.objects.all() \
				.filter(layoutitem_ptr__item_ptr__active=True).get(slug=person)
	except Person.DoesNotExist:
		raise Http404

	return person

def people_page(request, page, total=12, ajax=False):
	departments = _get_departments()
		
	try:
		people_list = Person.objects.all() \
			.filter(layoutitem_ptr__item_ptr__active=True)
			#.order_by('layoutitem_ptr__item_ptr__order') \
			#.order_by('layoutitem_ptr__item_ptr__title')
	except Person.DoesNotExist:
		raise Http404
	
	paginator = Paginator(people_list, total)

	try:
		page = int(request.GET.get('page', page))
	except ValueError:
		page = page	
	
	try:
		people = paginator.page(page)
	except (EmptyPage, InvalidPage):
		people = paginator.page(paginator.num_pages)
			
	temp = []
	for person in people.object_list:
		temp.insert(0, person)
	
	random.shuffle(temp)
	
	people.object_list = temp

	template = 'people/templates/people.html'
	if ajax:
		template = 'people.ajax'

	return render_to_response(template, {
			'people': people,
			'departments': departments,
			'pagination_width': paginator.num_pages * 26,
		}, context_instance=RequestContext(request)
	)

def department_page(request, slug, page=1, ajax=False):
	try: 
		department = Department.objects.all() \
			.filter(item_ptr__active=True).get(slug=slug)
	except Department.DoesNotExist:
		raise Http404
	
	try:
		people_list = Person.objects.all() \
			.filter(layoutitem_ptr__item_ptr__active=True) \
			.filter(department__exact=department)
			#.order_by('layoutitem_ptr__item_ptr__title')
	except Person.DoesNotExist:
		raise Http404
	
	paginator = Paginator(people_list, 18)

	try:
		page = int(request.GET.get('page', page))
	except ValueError:
		page = page	
	
	try:
		people = paginator.page(page)
	except (EmptyPage, InvalidPage):
		people = paginator.page(paginator.num_pages)
		
	temp = []
	for person in people.object_list:
		temp.insert(0, person)
	
	random.shuffle(temp)
	
	people.object_list = temp	
	
	template = 'people/templates/people.html'
	if ajax:
		template = 'people.ajax'

	return render_to_response(template, {
					'department': department,
					'people': people,
					'pagination_width': paginator.num_pages * 26,
		}, context_instance=RequestContext(request)
	)

def _get_departments():
	try:
		departments =  Department.objects.all() \
			.filter(item_ptr__active=True)
			#.order_by('item_ptr__title')
	except Department.DoesNotExist:
		raise Http404

	return departments