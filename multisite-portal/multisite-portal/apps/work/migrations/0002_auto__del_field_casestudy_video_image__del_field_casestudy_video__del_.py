# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models
from apps.work.models import CaseStudy

class Migration(SchemaMigration):
    no_dry_run = True
    
    def forwards(self, orm):
        
        # Adding field 'CaseStudyTranslation.title_i18n'
        db.add_column('work_casestudy_translation', 'title_i18n', self.gf('django.db.models.fields.CharField')(max_length=200, null=True), keep_default=False)

        # Adding field 'CaseStudyTranslation.hero_image'
        db.add_column('work_casestudy_translation', 'hero_image', self.gf('django.db.models.fields.files.FileField')(default='none', max_length=100), keep_default=False)

        # Adding field 'CaseStudyTranslation.video_image'
        db.add_column('work_casestudy_translation', 'video_image', self.gf('django.db.models.fields.files.FileField')(default='none', max_length=100), keep_default=False)

        # Adding field 'CaseStudyTranslation.video'
        db.add_column('work_casestudy_translation', 'video', self.gf('django.db.models.fields.files.FileField')(default='none', max_length=100), keep_default=False)

        for case in orm.CaseStudy.objects.all():
            trans = CaseStudy.Translation.objects.filter(master=case)
            for t in trans:
                t.hero_image = case.hero_image
                t.video_image = case.video_image
                t.video = case.video
                t.save()

        # Deleting field 'CaseStudy.video_image'
        db.delete_column('work_casestudy', 'video_image')

        # Deleting field 'CaseStudy.video'
        db.delete_column('work_casestudy', 'video')

        # Deleting field 'CaseStudy.hero_image'
        db.delete_column('work_casestudy', 'hero_image')


    def backwards(self, orm):
        

        # Adding field 'CaseStudy.video_image'
        db.add_column('work_casestudy', 'video_image', self.gf('django.db.models.fields.files.FileField')(default=0, max_length=100), keep_default=False)

        # Adding field 'CaseStudy.video'
        db.add_column('work_casestudy', 'video', self.gf('django.db.models.fields.files.FileField')(default=0, max_length=100), keep_default=False)

        # Adding field 'CaseStudy.hero_image'
        db.add_column('work_casestudy', 'hero_image', self.gf('django.db.models.fields.files.FileField')(default=0, max_length=100), keep_default=False)


        # Deleting field 'CaseStudyTranslation.title_i18n'
        db.delete_column('work_casestudy_translation', 'title_i18n')
        
        # Deleting field 'CaseStudyTranslation.hero_image'
        db.delete_column('work_casestudy_translation', 'hero_image')

        # Deleting field 'CaseStudyTranslation.video_image'
        db.delete_column('work_casestudy_translation', 'video_image')

        # Deleting field 'CaseStudyTranslation.video'
        db.delete_column('work_casestudy_translation', 'video')


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
        'work.award': {
            'Meta': {'object_name': 'Award'},
            'case_study': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'award_case_study'", 'to': "orm['work.CaseStudy']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'work.casestudy': {
            'Meta': {'object_name': 'CaseStudy', '_ormbases': ['home.LayoutItem']},
            'country': ('django.db.models.fields.CharField', [], {'default': "'ca'", 'max_length': '10', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['location.Agency']", 'null': 'True', 'blank': 'True'}),
            'external_db_id': ('django.db.models.fields.IntegerField', [], {'default': '-1', 'null': 'True', 'blank': 'True'}),
            'hero_image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'layoutitem_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['home.LayoutItem']", 'unique': 'True', 'primary_key': 'True'}),
            'posting_agency': ('django.db.models.fields.CharField', [], {'default': "'mindblossom Isobar'", 'max_length': '200'}),
            'publish_date': ('django.db.models.fields.DateField', [], {}),
            'publish_to_external': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'share_url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'video': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'video_image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },              
        'work.casestudytranslation': {
            'Meta': {'ordering': "('language_code',)", 'unique_together': "(('language_code', 'master'),)", 'object_name': 'CaseStudyTranslation', 'db_table': "'work_casestudy_translation'"},
            'body': ('apps.tinymce.models.HTMLField', [], {'blank': 'True'}),
            'hero_image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '15', 'blank': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'to': "orm['work.CaseStudy']"}),
            'title_i18n': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'video': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'video_image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['work']
