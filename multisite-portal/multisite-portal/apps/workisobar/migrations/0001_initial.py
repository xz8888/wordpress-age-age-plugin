# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'AwardTranslation'
        db.create_table('workisobar_award_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('language_code', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=15, blank=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', to=orm['workisobar.Award'])),
        ))
        db.send_create_signal('workisobar', ['AwardTranslation'])

        # Adding unique constraint on 'AwardTranslation', fields ['language_code', 'master']
        db.create_unique('workisobar_award_translation', ['language_code', 'master_id'])

        # Adding model 'Award'
        db.create_table('workisobar_award', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('casestudy', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='awards', null=True, to=orm['workisobar.CaseStudy'])),
            ('date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('workisobar', ['Award'])

        # Adding model 'ClientQuoteTranslation'
        db.create_table('workisobar_clientquote_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=15, blank=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', to=orm['workisobar.ClientQuote'])),
        ))
        db.send_create_signal('workisobar', ['ClientQuoteTranslation'])

        # Adding unique constraint on 'ClientQuoteTranslation', fields ['language_code', 'master']
        db.create_unique('workisobar_clientquote_translation', ['language_code', 'master_id'])

        # Adding model 'ClientQuote'
        db.create_table('workisobar_clientquote', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('casestudy', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='client_quotes', null=True, to=orm['workisobar.CaseStudy'])),
            ('date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('workisobar', ['ClientQuote'])

        # Adding model 'PressReleaseTranslation'
        db.create_table('workisobar_pressrelease_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=15, blank=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', to=orm['workisobar.PressRelease'])),
        ))
        db.send_create_signal('workisobar', ['PressReleaseTranslation'])

        # Adding unique constraint on 'PressReleaseTranslation', fields ['language_code', 'master']
        db.create_unique('workisobar_pressrelease_translation', ['language_code', 'master_id'])

        # Adding model 'PressRelease'
        db.create_table('workisobar_pressrelease', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('casestudy', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='press_releases', null=True, to=orm['workisobar.CaseStudy'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('workisobar', ['PressRelease'])

        # Adding model 'ClientsIndexTranslation'
        db.create_table('workisobar_clientsindex_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('meta_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=15, blank=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', to=orm['workisobar.ClientsIndex'])),
        ))
        db.send_create_signal('workisobar', ['ClientsIndexTranslation'])

        # Adding unique constraint on 'ClientsIndexTranslation', fields ['language_code', 'master']
        db.create_unique('workisobar_clientsindex_translation', ['language_code', 'master_id'])

        # Adding model 'ClientsIndex'
        db.create_table('workisobar_clientsindex', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('featured_video', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['video_promo.VideoPromo'], null=True, blank=True)),
        ))
        db.send_create_signal('workisobar', ['ClientsIndex'])

        # Adding model 'ClientsTranslation'
        db.create_table('workisobar_clients_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=15, blank=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', to=orm['workisobar.Clients'])),
        ))
        db.send_create_signal('workisobar', ['ClientsTranslation'])

        # Adding unique constraint on 'ClientsTranslation', fields ['language_code', 'master']
        db.create_unique('workisobar_clients_translation', ['language_code', 'master_id'])

        # Adding model 'Clients'
        db.create_table('workisobar_clients', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('featured', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('logo', self.gf('django.db.models.fields.files.FileField')(default='Enter a logo', max_length=100, blank=True)),
            ('client', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=999)),
        ))
        db.send_create_signal('workisobar', ['Clients'])

        # Adding model 'SlideShowItemTranslation'
        db.create_table('workisobar_slideshowitem_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=15, blank=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', to=orm['workisobar.SlideShowItem'])),
        ))
        db.send_create_signal('workisobar', ['SlideShowItemTranslation'])

        # Adding unique constraint on 'SlideShowItemTranslation', fields ['language_code', 'master']
        db.create_unique('workisobar_slideshowitem_translation', ['language_code', 'master_id'])

        # Adding model 'SlideShowItem'
        db.create_table('workisobar_slideshowitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image_id', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=999, blank=True)),
            ('casestudy', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='client_slide', null=True, to=orm['workisobar.CaseStudy'])),
        ))
        db.send_create_signal('workisobar', ['SlideShowItem'])

        # Adding model 'CaseStudyTranslation'
        db.create_table('workisobar_casestudy_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('body', self.gf('apps.tinymce.models.HTMLField')(blank=True)),
            ('hero_image', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('video_image', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('video', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=15, blank=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', to=orm['workisobar.CaseStudy'])),
        ))
        db.send_create_signal('workisobar', ['CaseStudyTranslation'])

        # Adding unique constraint on 'CaseStudyTranslation', fields ['language_code', 'master']
        db.create_unique('workisobar_casestudy_translation', ['language_code', 'master_id'])

        # Adding model 'CaseStudy'
        db.create_table('workisobar_casestudy', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
            ('title_id', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('publish_date', self.gf('django.db.models.fields.DateField')()),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=999, blank=True)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workisobar.Clients'], null=True, blank=True)),
            ('logo_sprite', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('homepage_image', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('workisobar', ['CaseStudy'])

        # Adding model 'CaseStudyIndexTranslation'
        db.create_table('workisobar_casestudyindex_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('meta_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=15, blank=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', to=orm['workisobar.CaseStudyIndex'])),
        ))
        db.send_create_signal('workisobar', ['CaseStudyIndexTranslation'])

        # Adding unique constraint on 'CaseStudyIndexTranslation', fields ['language_code', 'master']
        db.create_unique('workisobar_casestudyindex_translation', ['language_code', 'master_id'])

        # Adding model 'CaseStudyIndex'
        db.create_table('workisobar_casestudyindex', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('featured_video', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['video_promo.VideoPromo'], null=True, blank=True)),
        ))
        db.send_create_signal('workisobar', ['CaseStudyIndex'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'CaseStudyIndexTranslation', fields ['language_code', 'master']
        db.delete_unique('workisobar_casestudyindex_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'CaseStudyTranslation', fields ['language_code', 'master']
        db.delete_unique('workisobar_casestudy_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'SlideShowItemTranslation', fields ['language_code', 'master']
        db.delete_unique('workisobar_slideshowitem_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'ClientsTranslation', fields ['language_code', 'master']
        db.delete_unique('workisobar_clients_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'ClientsIndexTranslation', fields ['language_code', 'master']
        db.delete_unique('workisobar_clientsindex_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'PressReleaseTranslation', fields ['language_code', 'master']
        db.delete_unique('workisobar_pressrelease_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'ClientQuoteTranslation', fields ['language_code', 'master']
        db.delete_unique('workisobar_clientquote_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'AwardTranslation', fields ['language_code', 'master']
        db.delete_unique('workisobar_award_translation', ['language_code', 'master_id'])

        # Deleting model 'AwardTranslation'
        db.delete_table('workisobar_award_translation')

        # Deleting model 'Award'
        db.delete_table('workisobar_award')

        # Deleting model 'ClientQuoteTranslation'
        db.delete_table('workisobar_clientquote_translation')

        # Deleting model 'ClientQuote'
        db.delete_table('workisobar_clientquote')

        # Deleting model 'PressReleaseTranslation'
        db.delete_table('workisobar_pressrelease_translation')

        # Deleting model 'PressRelease'
        db.delete_table('workisobar_pressrelease')

        # Deleting model 'ClientsIndexTranslation'
        db.delete_table('workisobar_clientsindex_translation')

        # Deleting model 'ClientsIndex'
        db.delete_table('workisobar_clientsindex')

        # Deleting model 'ClientsTranslation'
        db.delete_table('workisobar_clients_translation')

        # Deleting model 'Clients'
        db.delete_table('workisobar_clients')

        # Deleting model 'SlideShowItemTranslation'
        db.delete_table('workisobar_slideshowitem_translation')

        # Deleting model 'SlideShowItem'
        db.delete_table('workisobar_slideshowitem')

        # Deleting model 'CaseStudyTranslation'
        db.delete_table('workisobar_casestudy_translation')

        # Deleting model 'CaseStudy'
        db.delete_table('workisobar_casestudy')

        # Deleting model 'CaseStudyIndexTranslation'
        db.delete_table('workisobar_casestudyindex_translation')

        # Deleting model 'CaseStudyIndex'
        db.delete_table('workisobar_casestudyindex')


    models = {
        'video_promo.videopromo': {
            'Meta': {'object_name': 'VideoPromo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '999', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'workisobar.award': {
            'Meta': {'object_name': 'Award'},
            'casestudy': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'awards'", 'null': 'True', 'to': "orm['workisobar.CaseStudy']"}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'workisobar.awardtranslation': {
            'Meta': {'ordering': "('language_code',)", 'unique_together': "(('language_code', 'master'),)", 'object_name': 'AwardTranslation', 'db_table': "'workisobar_award_translation'"},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '15', 'blank': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'to': "orm['workisobar.Award']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'workisobar.casestudy': {
            'Meta': {'ordering': "['order']", 'object_name': 'CaseStudy'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workisobar.Clients']", 'null': 'True', 'blank': 'True'}),
            'homepage_image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo_sprite': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '999', 'blank': 'True'}),
            'publish_date': ('django.db.models.fields.DateField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'title_id': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'workisobar.casestudyindex': {
            'Meta': {'object_name': 'CaseStudyIndex'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'featured_video': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['video_promo.VideoPromo']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'workisobar.casestudyindextranslation': {
            'Meta': {'ordering': "('language_code',)", 'unique_together': "(('language_code', 'master'),)", 'object_name': 'CaseStudyIndexTranslation', 'db_table': "'workisobar_casestudyindex_translation'"},
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '15', 'blank': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'to': "orm['workisobar.CaseStudyIndex']"}),
            'meta_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'workisobar.casestudytranslation': {
            'Meta': {'ordering': "('language_code',)", 'unique_together': "(('language_code', 'master'),)", 'object_name': 'CaseStudyTranslation', 'db_table': "'workisobar_casestudy_translation'"},
            'body': ('apps.tinymce.models.HTMLField', [], {'blank': 'True'}),
            'hero_image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '15', 'blank': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'to': "orm['workisobar.CaseStudy']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'video': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'video_image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        'workisobar.clientquote': {
            'Meta': {'object_name': 'ClientQuote'},
            'casestudy': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'client_quotes'", 'null': 'True', 'to': "orm['workisobar.CaseStudy']"}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'workisobar.clientquotetranslation': {
            'Meta': {'ordering': "('language_code',)", 'unique_together': "(('language_code', 'master'),)", 'object_name': 'ClientQuoteTranslation', 'db_table': "'workisobar_clientquote_translation'"},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '15', 'blank': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'to': "orm['workisobar.ClientQuote']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'workisobar.clients': {
            'Meta': {'object_name': 'Clients'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'client': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.FileField', [], {'default': "'Enter a logo'", 'max_length': '100', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '999'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'workisobar.clientsindex': {
            'Meta': {'object_name': 'ClientsIndex'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'featured_video': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['video_promo.VideoPromo']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'workisobar.clientsindextranslation': {
            'Meta': {'ordering': "('language_code',)", 'unique_together': "(('language_code', 'master'),)", 'object_name': 'ClientsIndexTranslation', 'db_table': "'workisobar_clientsindex_translation'"},
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '15', 'blank': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'to': "orm['workisobar.ClientsIndex']"}),
            'meta_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'workisobar.clientstranslation': {
            'Meta': {'ordering': "('language_code',)", 'unique_together': "(('language_code', 'master'),)", 'object_name': 'ClientsTranslation', 'db_table': "'workisobar_clients_translation'"},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '15', 'blank': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'to': "orm['workisobar.Clients']"})
        },
        'workisobar.pressrelease': {
            'Meta': {'object_name': 'PressRelease'},
            'casestudy': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'press_releases'", 'null': 'True', 'to': "orm['workisobar.CaseStudy']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'workisobar.pressreleasetranslation': {
            'Meta': {'ordering': "('language_code',)", 'unique_together': "(('language_code', 'master'),)", 'object_name': 'PressReleaseTranslation', 'db_table': "'workisobar_pressrelease_translation'"},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '15', 'blank': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'to': "orm['workisobar.PressRelease']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'workisobar.slideshowitem': {
            'Meta': {'ordering': "['order']", 'object_name': 'SlideShowItem'},
            'casestudy': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'client_slide'", 'null': 'True', 'to': "orm['workisobar.CaseStudy']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'image_id': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '999', 'blank': 'True'})
        },
        'workisobar.slideshowitemtranslation': {
            'Meta': {'ordering': "('language_code',)", 'unique_together': "(('language_code', 'master'),)", 'object_name': 'SlideShowItemTranslation', 'db_table': "'workisobar_slideshowitem_translation'"},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '15', 'blank': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'to': "orm['workisobar.SlideShowItem']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['workisobar']
