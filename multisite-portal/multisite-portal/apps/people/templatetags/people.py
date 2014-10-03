from apps.people.models import Department, Person
from django import template

register = template.Library()

@register.inclusion_tag('people/templates/departments_nav.html', takes_context=True)
def department_nav(context, additional_class= '', selected=False):
	departments =  Department.objects.all().filter(item_ptr__active=True).order_by('item_ptr__title')
	total_people = len(Person.objects.all().filter(layoutitem_ptr__item_ptr__active=True))
	
	return {
		'selected': selected,
		'additional_class': additional_class,
		'departments': departments,
		'total_people': total_people,
	}

@register.inclusion_tag('people/templates/person_tag.html', takes_context=True)
def render_person(context, person, size='small', department=False):

	return {
		'person': person,
		'size': size,
		'department': department,
		'settings': context['settings'],
	}

@register.filter
def display_as_big(counter):
	return ((counter + 11) % 12 == 0 or (counter + 6) % 12 == 0)