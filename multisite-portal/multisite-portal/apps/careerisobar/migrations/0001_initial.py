# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'CareerTranslation'
        db.create_table('careerisobar_career_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('meta_description', self.gf('django.db.models.fields.TextField')()),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('content', self.gf('apps.tinymce.models.HTMLField')(blank=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=15, blank=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', to=orm['careerisobar.Career'])),
        ))
        db.send_create_signal('careerisobar', ['CareerTranslation'])

        # Adding unique constraint on 'CareerTranslation', fields ['language_code', 'master']
        db.create_unique('careerisobar_career_translation', ['language_code', 'master_id'])

        # Adding model 'Career'
        db.create_table('careerisobar_career', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('careerisobar', ['Career'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'CareerTranslation', fields ['language_code', 'master']
        db.delete_unique('careerisobar_career_translation', ['language_code', 'master_id'])

        # Deleting model 'CareerTranslation'
        db.delete_table('careerisobar_career_translation')

        # Deleting model 'Career'
        db.delete_table('careerisobar_career')


    models = {
        'careerisobar.career': {
            'Meta': {'object_name': 'Career'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'careerisobar.careertranslation': {
            'Meta': {'ordering': "('language_code',)", 'unique_together': "(('language_code', 'master'),)", 'object_name': 'CareerTranslation', 'db_table': "'careerisobar_career_translation'"},
            'content': ('apps.tinymce.models.HTMLField', [], {'blank': 'True'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '15', 'blank': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'to': "orm['careerisobar.Career']"}),
            'meta_description': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['careerisobar']
