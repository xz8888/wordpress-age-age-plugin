# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models
from apps.about.models import About

class Migration(SchemaMigration):
    no_dry_run = True
    
    def forwards(self, orm):
        
        # Adding field 'AboutTranslation.video_image'
        db.add_column('about_about_translation', 'video_image', self.gf('django.db.models.fields.files.FileField')(default='n', max_length=100), keep_default=False)

        # Adding field 'AboutTranslation.video'
        db.add_column('about_about_translation', 'video', self.gf('django.db.models.fields.files.FileField')(default='n', max_length=100), keep_default=False)

        for about in orm.About.objects.all():
            ab = About.Translation.objects.filter(master=about)
            for a in ab:
                a.video_image = about.video_image
                a.video = about.video
                a.save()

        # Deleting field 'About.video_image'
        db.delete_column('about_about', 'video_image')

        # Deleting field 'About.video'
        db.delete_column('about_about', 'video')


    def backwards(self, orm):
        
        # Deleting field 'AboutTranslation.video_image'
        db.delete_column('about_about_translation', 'video_image')

        # Deleting field 'AboutTranslation.video'
        db.delete_column('about_about_translation', 'video')

        # Adding field 'About.video_image'
        db.add_column('about_about', 'video_image', self.gf('django.db.models.fields.files.FileField')(default='n', max_length=100), keep_default=False)

        # Adding field 'About.video'
        db.add_column('about_about', 'video', self.gf('django.db.models.fields.files.FileField')(default='n', max_length=100), keep_default=False)


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
            'tagline': ('apps.tinymce.models.HTMLField', [], {'blank': 'True'}),
            'video': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'video_image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['about']
