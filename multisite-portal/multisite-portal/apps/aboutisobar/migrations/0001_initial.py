# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ProfileTranslation'
        db.create_table('aboutisobar_profile_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('apps.tinymce.models.HTMLField')(max_length=1070, blank=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=15, blank=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', to=orm['aboutisobar.Profile'])),
        ))
        db.send_create_signal('aboutisobar', ['ProfileTranslation'])

        # Adding unique constraint on 'ProfileTranslation', fields ['language_code', 'master']
        db.create_unique('aboutisobar_profile_translation', ['language_code', 'master_id'])

        # Adding model 'Profile'
        db.create_table('aboutisobar_profile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=999)),
        ))
        db.send_create_signal('aboutisobar', ['Profile'])

        # Adding model 'Partner'
        db.create_table('aboutisobar_partner', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('description', self.gf('django.db.models.fields.CharField')(default='Default', max_length=270)),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('aboutisobar', ['Partner'])

        # Adding model 'ServiceTranslation'
        db.create_table('aboutisobar_service_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('short_description', self.gf('apps.tinymce.models.HTMLField')(blank=True)),
            ('long_description', self.gf('apps.tinymce.models.HTMLField')(blank=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=15, blank=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', to=orm['aboutisobar.Service'])),
        ))
        db.send_create_signal('aboutisobar', ['ServiceTranslation'])

        # Adding unique constraint on 'ServiceTranslation', fields ['language_code', 'master']
        db.create_unique('aboutisobar_service_translation', ['language_code', 'master_id'])

        # Adding model 'Service'
        db.create_table('aboutisobar_service', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=999)),
        ))
        db.send_create_signal('aboutisobar', ['Service'])

        # Adding model 'AboutTranslation'
        db.create_table('aboutisobar_about_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('meta_description', self.gf('django.db.models.fields.TextField')()),
            ('language_code', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=15, blank=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', to=orm['aboutisobar.About'])),
        ))
        db.send_create_signal('aboutisobar', ['AboutTranslation'])

        # Adding unique constraint on 'AboutTranslation', fields ['language_code', 'master']
        db.create_unique('aboutisobar_about_translation', ['language_code', 'master_id'])

        # Adding model 'About'
        db.create_table('aboutisobar_about', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('featured_slogan', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('profiles_text', self.gf('apps.tinymce.models.HTMLField')(blank=True)),
            ('featured_video', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['video_promo.VideoPromo'], null=True, blank=True)),
        ))
        db.send_create_signal('aboutisobar', ['About'])

        # Adding M2M table for field profiles on 'About'
        db.create_table('aboutisobar_about_profiles', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('about', models.ForeignKey(orm['aboutisobar.about'], null=False)),
            ('profile', models.ForeignKey(orm['aboutisobar.profile'], null=False))
        ))
        db.create_unique('aboutisobar_about_profiles', ['about_id', 'profile_id'])

        # Adding M2M table for field partners on 'About'
        db.create_table('aboutisobar_about_partners', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('about', models.ForeignKey(orm['aboutisobar.about'], null=False)),
            ('partner', models.ForeignKey(orm['aboutisobar.partner'], null=False))
        ))
        db.create_unique('aboutisobar_about_partners', ['about_id', 'partner_id'])

        # Adding M2M table for field services on 'About'
        db.create_table('aboutisobar_about_services', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('about', models.ForeignKey(orm['aboutisobar.about'], null=False)),
            ('service', models.ForeignKey(orm['aboutisobar.service'], null=False))
        ))
        db.create_unique('aboutisobar_about_services', ['about_id', 'service_id'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'AboutTranslation', fields ['language_code', 'master']
        db.delete_unique('aboutisobar_about_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'ServiceTranslation', fields ['language_code', 'master']
        db.delete_unique('aboutisobar_service_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'ProfileTranslation', fields ['language_code', 'master']
        db.delete_unique('aboutisobar_profile_translation', ['language_code', 'master_id'])

        # Deleting model 'ProfileTranslation'
        db.delete_table('aboutisobar_profile_translation')

        # Deleting model 'Profile'
        db.delete_table('aboutisobar_profile')

        # Deleting model 'Partner'
        db.delete_table('aboutisobar_partner')

        # Deleting model 'ServiceTranslation'
        db.delete_table('aboutisobar_service_translation')

        # Deleting model 'Service'
        db.delete_table('aboutisobar_service')

        # Deleting model 'AboutTranslation'
        db.delete_table('aboutisobar_about_translation')

        # Deleting model 'About'
        db.delete_table('aboutisobar_about')

        # Removing M2M table for field profiles on 'About'
        db.delete_table('aboutisobar_about_profiles')

        # Removing M2M table for field partners on 'About'
        db.delete_table('aboutisobar_about_partners')

        # Removing M2M table for field services on 'About'
        db.delete_table('aboutisobar_about_services')


    models = {
        'aboutisobar.about': {
            'Meta': {'ordering': "['title']", 'object_name': 'About'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'featured_slogan': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'featured_video': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['video_promo.VideoPromo']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'partners': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'partner_about'", 'symmetrical': 'False', 'to': "orm['aboutisobar.Partner']"}),
            'profiles': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'profile_about'", 'symmetrical': 'False', 'to': "orm['aboutisobar.Profile']"}),
            'profiles_text': ('apps.tinymce.models.HTMLField', [], {'blank': 'True'}),
            'services': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'service_about'", 'symmetrical': 'False', 'to': "orm['aboutisobar.Service']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'aboutisobar.abouttranslation': {
            'Meta': {'ordering': "('language_code',)", 'unique_together': "(('language_code', 'master'),)", 'object_name': 'AboutTranslation', 'db_table': "'aboutisobar_about_translation'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '15', 'blank': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'to': "orm['aboutisobar.About']"}),
            'meta_description': ('django.db.models.fields.TextField', [], {})
        },
        'aboutisobar.partner': {
            'Meta': {'ordering': "['title']", 'object_name': 'Partner'},
            'description': ('django.db.models.fields.CharField', [], {'default': "'Default'", 'max_length': '270'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'aboutisobar.profile': {
            'Meta': {'ordering': "['order']", 'object_name': 'Profile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '999'})
        },
        'aboutisobar.profiletranslation': {
            'Meta': {'ordering': "('language_code',)", 'unique_together': "(('language_code', 'master'),)", 'object_name': 'ProfileTranslation', 'db_table': "'aboutisobar_profile_translation'"},
            'description': ('apps.tinymce.models.HTMLField', [], {'max_length': '1070', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '15', 'blank': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'to': "orm['aboutisobar.Profile']"})
        },
        'aboutisobar.service': {
            'Meta': {'ordering': "['order']", 'object_name': 'Service'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '999'})
        },
        'aboutisobar.servicetranslation': {
            'Meta': {'ordering': "('language_code',)", 'unique_together': "(('language_code', 'master'),)", 'object_name': 'ServiceTranslation', 'db_table': "'aboutisobar_service_translation'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '15', 'blank': 'True'}),
            'long_description': ('apps.tinymce.models.HTMLField', [], {'blank': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'to': "orm['aboutisobar.Service']"}),
            'short_description': ('apps.tinymce.models.HTMLField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'video_promo.videopromo': {
            'Meta': {'object_name': 'VideoPromo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '999', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['aboutisobar']
