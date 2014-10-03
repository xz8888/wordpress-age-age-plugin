# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'JobTranslation'
        db.create_table('jobs_job_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('body', self.gf('apps.tinymce.models.HTMLField')(blank=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=15, blank=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', to=orm['jobs.Job'])),
        ))
        db.send_create_signal('jobs', ['JobTranslation'])

        # Adding unique constraint on 'JobTranslation', fields ['language_code', 'master']
        db.create_unique('jobs_job_translation', ['language_code', 'master_id'])

        # Adding model 'Job'
        db.create_table('jobs_job', (
            ('item_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['common.Item'], unique=True, primary_key=True)),
            ('contact', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
            ('specification', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('jobs', ['Job'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'JobTranslation', fields ['language_code', 'master']
        db.delete_unique('jobs_job_translation', ['language_code', 'master_id'])

        # Deleting model 'JobTranslation'
        db.delete_table('jobs_job_translation')

        # Deleting model 'Job'
        db.delete_table('jobs_job')


    models = {
        'common.item': {
            'Meta': {'object_name': 'Item'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '999'}),
            'subclass': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'jobs.job': {
            'Meta': {'object_name': 'Job', '_ormbases': ['common.Item']},
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'item_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['common.Item']", 'unique': 'True', 'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'specification': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
        },
        'jobs.jobtranslation': {
            'Meta': {'ordering': "('language_code',)", 'unique_together': "(('language_code', 'master'),)", 'object_name': 'JobTranslation', 'db_table': "'jobs_job_translation'"},
            'body': ('apps.tinymce.models.HTMLField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '15', 'blank': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'to': "orm['jobs.Job']"})
        }
    }

    complete_apps = ['jobs']
