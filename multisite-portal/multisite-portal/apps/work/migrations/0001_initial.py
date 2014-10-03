# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'CaseStudyTranslation'
        db.create_table('work_casestudy_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('body', self.gf('apps.tinymce.models.HTMLField')(blank=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=15, blank=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', to=orm['work.CaseStudy'])),
        ))
        db.send_create_signal('work', ['CaseStudyTranslation'])

        # Adding unique constraint on 'CaseStudyTranslation', fields ['language_code', 'master']
        db.create_unique('work_casestudy_translation', ['language_code', 'master_id'])

        # Adding model 'CaseStudy'
        db.create_table('work_casestudy', (
            ('layoutitem_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['home.LayoutItem'], unique=True, primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['location.Agency'], null=True, blank=True)),
            ('hero_image', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('video_image', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('video', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('publish_date', self.gf('django.db.models.fields.DateField')()),
            ('country', self.gf('django.db.models.fields.CharField')(default='ca', max_length=10, blank=True)),
            ('external_db_id', self.gf('django.db.models.fields.IntegerField')(default=-1, null=True, blank=True)),
            ('publish_to_external', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('posting_agency', self.gf('django.db.models.fields.CharField')(default='mindblossom Isobar', max_length=200)),
            ('share_url', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('work', ['CaseStudy'])

        # Adding model 'Award'
        db.create_table('work_award', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('case_study', self.gf('django.db.models.fields.related.ForeignKey')(related_name='award_case_study', to=orm['work.CaseStudy'])),
        ))
        db.send_create_signal('work', ['Award'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'CaseStudyTranslation', fields ['language_code', 'master']
        db.delete_unique('work_casestudy_translation', ['language_code', 'master_id'])

        # Deleting model 'CaseStudyTranslation'
        db.delete_table('work_casestudy_translation')

        # Deleting model 'CaseStudy'
        db.delete_table('work_casestudy')

        # Deleting model 'Award'
        db.delete_table('work_award')


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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '15', 'blank': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'to': "orm['work.CaseStudy']"})
        }
    }

    complete_apps = ['work']
