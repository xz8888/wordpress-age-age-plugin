from django.db import models
from apps.common.models import Item

class LayoutItem(Item):
	def __unicode__(self):
		title = self.title
		return title

class Layout(models.Model):
	# Imports are inside the class due to dependency between Story and
	# LayoutItem
	from apps.work.models import CaseStudy
	from apps.news.models import Story

	case_study_large_1 = models.ForeignKey(CaseStudy, related_name='case_study_large_1_layout')
	case_study_large_2 = models.ForeignKey(CaseStudy, related_name='case_study_large_2_layout')
	case_study_large_3 = models.ForeignKey(CaseStudy, related_name='case_study_large_3_layout')
	case_study_small_1 = models.ForeignKey(CaseStudy, related_name='case_study_small_1_layout')
	case_study_small_2 = models.ForeignKey(CaseStudy, related_name='case_study_small_2_layout')
	case_study_small_3 = models.ForeignKey(CaseStudy, related_name='case_study_small_3_layout')
	news_story_1 = models.ForeignKey(Story, related_name='news_story_1_layout')
	news_story_2 = models.ForeignKey(Story, related_name='news_story_2_layout')
	
	def __unicode__(self):
		return str('Layout')
	