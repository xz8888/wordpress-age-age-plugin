"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from apps.common.models import Item
from apps.jobs.models import Job
import datetime

class JobsTest(TestCase):
	
  def test_job(self):
  	self.job = Job.objects.create(title="Job 1", slug="job-1", contact='test@example.com', specification='/docs/spec.doc', body='job body')
  	
  	c  = Client(enforce_csrd_checks=True)
	response = c.get(self.job.get_absolute_url())
	
	self.assertEqual(response.status_code, 200)
	self.assertEqual(response.context['job'], self.job)
	
	
  def test_jobs(self):
  	self.job1 = Job.objects.create(title="Job 1", slug="job-1", contact='test@example.com', specification='/docs/spec.doc', body='job body 1')
  	self.job2 = Job.objects.create(title="Job 2", slug="job-2", contact='test@example.com', specification='/docs/spec.doc', body='job body 2')
  	self.job3 = Job.objects.create(title="Job 3", slug="job-3", contact='test@example.com', specification='/docs/spec.doc', body='job body 3')
  	
	c  = Client(enforce_csrd_checks=True)
	response = c.get('/jobs/')
	
	print response.content
	
	self.assertEqual(response.status_code, 200)
	self.assertEqual(len(response.context['jobs']), 3)