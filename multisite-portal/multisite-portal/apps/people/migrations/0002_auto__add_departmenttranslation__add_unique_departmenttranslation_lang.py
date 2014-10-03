# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'DepartmentTranslation'
        db.create_table('people_department_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title_i18n', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=15, blank=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', to=orm['people.Department'])),
        ))
        db.send_create_signal('people', ['DepartmentTranslation'])

        # Adding unique constraint on 'DepartmentTranslation', fields ['language_code', 'master']
        db.create_unique('people_department_translation', ['language_code', 'master_id'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'DepartmentTranslation', fields ['language_code', 'master']
        db.delete_unique('people_department_translation', ['language_code', 'master_id'])

        # Deleting model 'DepartmentTranslation'
        db.delete_table('people_department_translation')


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
        'home.layoutitem': {
            'Meta': {'object_name': 'LayoutItem', '_ormbases': ['common.Item']},
            'item_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['common.Item']", 'unique': 'True', 'primary_key': 'True'})
        },
        'people.department': {
            'Meta': {'object_name': 'Department', '_ormbases': ['common.Item']},
            'colour': ('django.db.models.fields.CharField', [], {'default': "'#ff0000'", 'max_length': '7'}),
            'item_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['common.Item']", 'unique': 'True', 'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        'people.departmenttranslation': {
            'Meta': {'ordering': "('language_code',)", 'unique_together': "(('language_code', 'master'),)", 'object_name': 'DepartmentTranslation', 'db_table': "'people_department_translation'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '15', 'blank': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'to': "orm['people.Department']"}),
            'title_i18n': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'people.person': {
            'Meta': {'object_name': 'Person', '_ormbases': ['home.LayoutItem']},
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.Department']"}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'layoutitem_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['home.LayoutItem']", 'unique': 'True', 'primary_key': 'True'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        'people.persontranslation': {
            'Meta': {'ordering': "('language_code',)", 'unique_together': "(('language_code', 'master'),)", 'object_name': 'PersonTranslation', 'db_table': "'people_person_translation'"},
            'body': ('apps.tinymce.models.HTMLField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '15', 'blank': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'to': "orm['people.Person']"})
        }
    }

    complete_apps = ['people']
