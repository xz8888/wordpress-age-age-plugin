# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models
from apps.news.models import Story

class Migration(SchemaMigration):
    no_dry_run = True
    
    def forwards(self, orm):
        
        # Adding field 'StoryTranslation.title_i18n'
        db.add_column('news_story_translation', 'title_i18n', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'StoryTranslation.image'
        db.add_column('news_story_translation', 'image', self.gf('django.db.models.fields.files.FileField')(default='', max_length=100, blank=True), keep_default=False)

        for story in orm.Story.objects.all():
            st = Story.Translation.objects.filter(master=story)
            for s in st:
                s.image = story.image
                s.save()

        # Deleting field 'Story.image'
        db.delete_column('news_story', 'image')


    def backwards(self, orm):
        
        # Deleting field 'StoryTranslation.title_i18n'
        db.delete_column('news_story_translation', 'title_i18n')

        # Deleting field 'StoryTranslation.image'
        db.delete_column('news_story_translation', 'image')

        # Adding field 'Story.image'
        db.add_column('news_story', 'image', self.gf('django.db.models.fields.files.FileField')(default='', max_length=100, blank=True), keep_default=False)


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
        'location.agency': {
            'Meta': {'object_name': 'Agency'},
            'address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'body': ('apps.tinymce.models.HTMLField', [], {'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['location.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'location.country': {
            'Meta': {'object_name': 'Country'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'zoom_level': ('django.db.models.fields.CharField', [], {'default': "'5'", 'max_length': '2'})
        },
        'news.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'news.friend': {
            'Meta': {'object_name': 'Friend'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'news.relatedlink': {
            'Meta': {'object_name': 'RelatedLink'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'story': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'related_link_story'", 'to': "orm['news.Story']"}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'news.story': {
            'Meta': {'object_name': 'Story', '_ormbases': ['home.LayoutItem']},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.Person']", 'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['news.Category']", 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'default': "'ca'", 'max_length': '10', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['location.Agency']", 'null': 'True', 'blank': 'True'}),
            'external_db_id': ('django.db.models.fields.IntegerField', [], {'default': '-1', 'null': 'True', 'blank': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'layoutitem_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['home.LayoutItem']", 'unique': 'True', 'primary_key': 'True'}),
            'posting_agency': ('django.db.models.fields.CharField', [], {'default': "'mindblossom Isobar'", 'max_length': '200'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {}),
            'publish_to_external': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'sticky': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'news.storytranslation': {
            'Meta': {'ordering': "('language_code',)", 'unique_together': "(('language_code', 'master'),)", 'object_name': 'StoryTranslation', 'db_table': "'news_story_translation'"},
            'body': ('apps.tinymce.models.HTMLField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '15', 'blank': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'to': "orm['news.Story']"}),
            'title_i18n': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'people.department': {
            'Meta': {'object_name': 'Department', '_ormbases': ['common.Item']},
            'colour': ('django.db.models.fields.CharField', [], {'default': "'#ff0000'", 'max_length': '7'}),
            'item_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['common.Item']", 'unique': 'True', 'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        'people.person': {
            'Meta': {'object_name': 'Person', '_ormbases': ['home.LayoutItem']},
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.Department']"}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'layoutitem_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['home.LayoutItem']", 'unique': 'True', 'primary_key': 'True'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['news']
