# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'VideoPromoTranslation'
        db.create_table('video_promo_videopromo_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('body', self.gf('apps.tinymce.models.HTMLField')(blank=True)),
            ('link_text', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('hero_image', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('video_image', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('video', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=15, blank=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', to=orm['video_promo.VideoPromo'])),
        ))
        db.send_create_signal('video_promo', ['VideoPromoTranslation'])

        # Adding unique constraint on 'VideoPromoTranslation', fields ['language_code', 'master']
        db.create_unique('video_promo_videopromo_translation', ['language_code', 'master_id'])

        # Adding model 'VideoPromo'
        db.create_table('video_promo_videopromo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=999, blank=True)),
        ))
        db.send_create_signal('video_promo', ['VideoPromo'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'VideoPromoTranslation', fields ['language_code', 'master']
        db.delete_unique('video_promo_videopromo_translation', ['language_code', 'master_id'])

        # Deleting model 'VideoPromoTranslation'
        db.delete_table('video_promo_videopromo_translation')

        # Deleting model 'VideoPromo'
        db.delete_table('video_promo_videopromo')


    models = {
        'video_promo.videopromo': {
            'Meta': {'object_name': 'VideoPromo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '999', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'video_promo.videopromotranslation': {
            'Meta': {'ordering': "('language_code',)", 'unique_together': "(('language_code', 'master'),)", 'object_name': 'VideoPromoTranslation', 'db_table': "'video_promo_videopromo_translation'"},
            'body': ('apps.tinymce.models.HTMLField', [], {'blank': 'True'}),
            'hero_image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '15', 'blank': 'True'}),
            'link_text': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'to': "orm['video_promo.VideoPromo']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'video': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'video_image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['video_promo']
