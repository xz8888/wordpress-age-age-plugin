# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'HomeTranslation'
        db.create_table('homeisobar_home_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('meta_description', self.gf('django.db.models.fields.TextField')()),
            ('language_code', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=15, blank=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', to=orm['homeisobar.Home'])),
        ))
        db.send_create_signal('homeisobar', ['HomeTranslation'])

        # Adding unique constraint on 'HomeTranslation', fields ['language_code', 'master']
        db.create_unique('homeisobar_home_translation', ['language_code', 'master_id'])

        # Adding model 'Home'
        db.create_table('homeisobar_home', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('featured_news_1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='featured_story_1', to=orm['news.Story'])),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('homeisobar', ['Home'])

        # Adding M2M table for field featured_case_studies on 'Home'
        db.create_table('homeisobar_home_featured_case_studies', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('home', models.ForeignKey(orm['homeisobar.home'], null=False)),
            ('casestudy', models.ForeignKey(orm['workisobar.casestudy'], null=False))
        ))
        db.create_unique('homeisobar_home_featured_case_studies', ['home_id', 'casestudy_id'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'HomeTranslation', fields ['language_code', 'master']
        db.delete_unique('homeisobar_home_translation', ['language_code', 'master_id'])

        # Deleting model 'HomeTranslation'
        db.delete_table('homeisobar_home_translation')

        # Deleting model 'Home'
        db.delete_table('homeisobar_home')

        # Removing M2M table for field featured_case_studies on 'Home'
        db.delete_table('homeisobar_home_featured_case_studies')


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
        'homeisobar.home': {
            'Meta': {'object_name': 'Home'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'featured_case_studies': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['workisobar.CaseStudy']", 'null': 'True', 'blank': 'True'}),
            'featured_news_1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'featured_story_1'", 'to': "orm['news.Story']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'homeisobar.hometranslation': {
            'Meta': {'ordering': "('language_code',)", 'unique_together': "(('language_code', 'master'),)", 'object_name': 'HomeTranslation', 'db_table': "'homeisobar_home_translation'"},
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '15', 'blank': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'to': "orm['homeisobar.Home']"}),
            'meta_description': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
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
        'news.story': {
            'Meta': {'object_name': 'Story', '_ormbases': ['home.LayoutItem']},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['people.Person']", 'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['news.Category']", 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'default': "'us2'", 'max_length': '10', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['location.Agency']", 'null': 'True', 'blank': 'True'}),
            'external_db_id': ('django.db.models.fields.IntegerField', [], {'default': '-1', 'null': 'True', 'blank': 'True'}),
            'layoutitem_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['home.LayoutItem']", 'unique': 'True', 'primary_key': 'True'}),
            'posting_agency': ('django.db.models.fields.CharField', [], {'default': "'roundarch isobar'", 'max_length': '200'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {}),
            'publish_to_external': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'show_homepage_thumbnail': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'sticky': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
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
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
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
        'workisobar.clients': {
            'Meta': {'object_name': 'Clients'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'client': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.FileField', [], {'default': "'Enter a logo'", 'max_length': '100', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '999'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['homeisobar']
