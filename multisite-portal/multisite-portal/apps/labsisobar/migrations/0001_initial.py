# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'PartnershipTranslation'
        db.create_table('labsisobar_partnership_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('apps.tinymce.models.HTMLField')(blank=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=15, blank=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', to=orm['labsisobar.Partnership'])),
        ))
        db.send_create_signal('labsisobar', ['PartnershipTranslation'])

        # Adding unique constraint on 'PartnershipTranslation', fields ['language_code', 'master']
        db.create_unique('labsisobar_partnership_translation', ['language_code', 'master_id'])

        # Adding model 'Partnership'
        db.create_table('labsisobar_partnership', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('remove_image', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('labsisobar', ['Partnership'])

        # Adding model 'LabsIndexTranslation'
        db.create_table('labsisobar_labsindex_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('meta_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=15, blank=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', to=orm['labsisobar.LabsIndex'])),
        ))
        db.send_create_signal('labsisobar', ['LabsIndexTranslation'])

        # Adding unique constraint on 'LabsIndexTranslation', fields ['language_code', 'master']
        db.create_unique('labsisobar_labsindex_translation', ['language_code', 'master_id'])

        # Adding model 'LabsIndex'
        db.create_table('labsisobar_labsindex', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('featured_video', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['video_promo.VideoPromo'], null=True, blank=True)),
        ))
        db.send_create_signal('labsisobar', ['LabsIndex'])

        # Adding M2M table for field partnerships on 'LabsIndex'
        db.create_table('labsisobar_labsindex_partnerships', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('labsindex', models.ForeignKey(orm['labsisobar.labsindex'], null=False)),
            ('partnership', models.ForeignKey(orm['labsisobar.partnership'], null=False))
        ))
        db.create_unique('labsisobar_labsindex_partnerships', ['labsindex_id', 'partnership_id'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'LabsIndexTranslation', fields ['language_code', 'master']
        db.delete_unique('labsisobar_labsindex_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'PartnershipTranslation', fields ['language_code', 'master']
        db.delete_unique('labsisobar_partnership_translation', ['language_code', 'master_id'])

        # Deleting model 'PartnershipTranslation'
        db.delete_table('labsisobar_partnership_translation')

        # Deleting model 'Partnership'
        db.delete_table('labsisobar_partnership')

        # Deleting model 'LabsIndexTranslation'
        db.delete_table('labsisobar_labsindex_translation')

        # Deleting model 'LabsIndex'
        db.delete_table('labsisobar_labsindex')

        # Removing M2M table for field partnerships on 'LabsIndex'
        db.delete_table('labsisobar_labsindex_partnerships')


    models = {
        'labsisobar.labsindex': {
            'Meta': {'object_name': 'LabsIndex'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'featured_video': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['video_promo.VideoPromo']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'partnerships': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'partnership'", 'symmetrical': 'False', 'to': "orm['labsisobar.Partnership']"})
        },
        'labsisobar.labsindextranslation': {
            'Meta': {'ordering': "('language_code',)", 'unique_together': "(('language_code', 'master'),)", 'object_name': 'LabsIndexTranslation', 'db_table': "'labsisobar_labsindex_translation'"},
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '15', 'blank': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'to': "orm['labsisobar.LabsIndex']"}),
            'meta_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'labsisobar.partnership': {
            'Meta': {'object_name': 'Partnership'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'remove_image': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'labsisobar.partnershiptranslation': {
            'Meta': {'ordering': "('language_code',)", 'unique_together': "(('language_code', 'master'),)", 'object_name': 'PartnershipTranslation', 'db_table': "'labsisobar_partnership_translation'"},
            'description': ('apps.tinymce.models.HTMLField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '15', 'blank': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'to': "orm['labsisobar.Partnership']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'video_promo.videopromo': {
            'Meta': {'object_name': 'VideoPromo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '999', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['labsisobar']
