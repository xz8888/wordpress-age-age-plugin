# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'AboutTranslation.video'
        db.alter_column('about_about_translation', 'video', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True))

    def backwards(self, orm):
        
        # Changing field 'AboutTranslation.video'
        db.alter_column('about_about_translation', 'video', self.gf('django.db.models.fields.files.FileField')(default='', max_length=100))

    models = {
        'about.about': {
            'Meta': {'object_name': 'About'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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
            'tagline': ('apps.tinymce.models.HTMLField', [], {'blank': 'True'}),
            'video': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'video_image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['about']
