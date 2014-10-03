# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'AboutTranslation'
        db.create_table('about_about_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tagline', self.gf('apps.tinymce.models.HTMLField')(blank=True)),
            ('left_header', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('left_body', self.gf('apps.tinymce.models.HTMLField')(blank=True)),
            ('right_header', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('right_body', self.gf('apps.tinymce.models.HTMLField')(blank=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=15, blank=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', to=orm['about.About'])),
        ))
        db.send_create_signal('about', ['AboutTranslation'])

        # Adding unique constraint on 'AboutTranslation', fields ['language_code', 'master']
        db.create_unique('about_about_translation', ['language_code', 'master_id'])

        # Adding model 'About'
        db.create_table('about_about', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('video_image', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('video', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('about', ['About'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'AboutTranslation', fields ['language_code', 'master']
        db.delete_unique('about_about_translation', ['language_code', 'master_id'])

        # Deleting model 'AboutTranslation'
        db.delete_table('about_about_translation')

        # Deleting model 'About'
        db.delete_table('about_about')


    models = {
        'about.about': {
            'Meta': {'object_name': 'About'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'video': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'video_image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        'about.abouttranslation': {
            'Meta': {'ordering': "('language_code',)", 'unique_together': "(('language_code', 'master'),)", 'object_name': 'AboutTranslation', 'db_table': "'about_about_translation'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '15', 'blank': 'True'}),
            'left_body': ('apps.tinymce.models.HTMLField', [], {'blank': 'True'}),
            'left_header': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'to': "orm['about.About']"}),
            'right_body': ('apps.tinymce.models.HTMLField', [], {'blank': 'True'}),
            'right_header': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tagline': ('apps.tinymce.models.HTMLField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['about']
