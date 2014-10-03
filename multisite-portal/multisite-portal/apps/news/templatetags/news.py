from apps.news.models import Category, Story, Category, Friend
from apps.social.models import PosterousPost, PosterousAccount, TwitterTweet, \
	PromoBox
from django import template
import settings

register = template.Library()

@register.inclusion_tag('news/templates/news_nav.html', takes_context=True)
def news_nav(context, additional_class= '', selected=False):
	categories = Category.objects.all().order_by('title')

	try:
		promo = PromoBox.objects.all()[:1][0]
	except:
		promo = None

	return {
		'selected': selected,
		'additional_class': additional_class,
		'categories': categories,
		'promo': promo,
		'settings': context['settings'],
	}

@register.inclusion_tag('news/templates/news_small_item.html', takes_context=True)
def news_small_item(context, item):
	return {
		'item': item,
		'request': context['request'],
		'settings': context['settings'],
	}

@register.inclusion_tag('news/templates/posted_by.html', takes_context=True)
def posted_by(context, story, show_department, author_size):
	return {
		'story': story,
		'show_department': show_department,
		'author_size': author_size,
		'request': context['request'],
		'settings': context['settings'],
	}

@register.inclusion_tag('news/templates/posted_by_small_item.html', takes_context=True)
def posted_by_small_item(context, story):
	return {
		'item': story,
		'request': context['request'],
		'settings': context['settings'],
	}

@register.inclusion_tag('news/templates/news_twitter.html', takes_context=True)
def news_twitter(context):
	tweets = TwitterTweet.objects.all().order_by('-created')[:5]

	return {
		'tweets': tweets,
	}

@register.inclusion_tag('news/templates/news_posterous.html', takes_context=True)
def news_posterous(context):
	try:
		account = PosterousAccount.objects.all()[:1][0]
		posts = PosterousPost.objects.all().order_by('-created')[:5]
	except:
		posts = None
		account = None

	return {
		'posts': posts,
		'account': account
	}
	
@register.inclusion_tag('news/templates/news_friends.html', takes_context=True)
def news_friends(context):
	friends = Friend.objects.all().order_by('title')

	return {
		'friends': friends,
	}
	
@register.inclusion_tag('news/templates/news_promo_box.html', takes_context=True)
def news_promo_box(context):
	promo = None

	try:
		promo = PromoBox.objects.all()[:1][0]
	except:
		print 'no promo box information'
	
	return {
		'promo': promo,
	}