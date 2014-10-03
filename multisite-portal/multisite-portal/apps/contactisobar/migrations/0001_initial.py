# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Office'
        db.create_table('contactisobar_office', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('address_line1', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('address_line2', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('latitude', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('longitude', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('show', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('contactisobar', ['Office'])

        # Adding model 'Country'
        db.create_table('contactisobar_country', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=999)),
        ))
        db.send_create_signal('contactisobar', ['Country'])

        # Adding M2M table for field offices on 'Country'
        db.create_table('contactisobar_country_offices', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('country', models.ForeignKey(orm['contactisobar.country'], null=False)),
            ('office', models.ForeignKey(orm['contactisobar.office'], null=False))
        ))
        db.create_unique('contactisobar_country_offices', ['country_id', 'office_id'])

        # Adding model 'Person'
        db.create_table('contactisobar_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=100, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=999)),
        ))
        db.send_create_signal('contactisobar', ['Person'])

        # Adding model 'Region'
        db.create_table('contactisobar_region', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=999)),
        ))
        db.send_create_signal('contactisobar', ['Region'])

        # Adding M2M table for field people on 'Region'
        db.create_table('contactisobar_region_people', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('region', models.ForeignKey(orm['contactisobar.region'], null=False)),
            ('person', models.ForeignKey(orm['contactisobar.person'], null=False))
        ))
        db.create_unique('contactisobar_region_people', ['region_id', 'person_id'])

        # Adding M2M table for field countries on 'Region'
        db.create_table('contactisobar_region_countries', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('region', models.ForeignKey(orm['contactisobar.region'], null=False)),
            ('country', models.ForeignKey(orm['contactisobar.country'], null=False))
        ))
        db.create_unique('contactisobar_region_countries', ['region_id', 'country_id'])


    def backwards(self, orm):
        
        # Deleting model 'Office'
        db.delete_table('contactisobar_office')

        # Deleting model 'Country'
        db.delete_table('contactisobar_country')

        # Removing M2M table for field offices on 'Country'
        db.delete_table('contactisobar_country_offices')

        # Deleting model 'Person'
        db.delete_table('contactisobar_person')

        # Deleting model 'Region'
        db.delete_table('contactisobar_region')

        # Removing M2M table for field people on 'Region'
        db.delete_table('contactisobar_region_people')

        # Removing M2M table for field countries on 'Region'
        db.delete_table('contactisobar_region_countries')


    models = {
        'contactisobar.country': {
            'Meta': {'ordering': "['order', 'name']", 'object_name': 'Country'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'offices': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'offices'", 'symmetrical': 'False', 'to': "orm['contactisobar.Office']"}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '999'})
        },
        'contactisobar.office': {
            'Meta': {'ordering': "['name']", 'object_name': 'Office'},
            'address_line1': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'address_line2': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'show': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'contactisobar.person': {
            'Meta': {'ordering': "['order']", 'object_name': 'Person'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '999'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'contactisobar.region': {
            'Meta': {'ordering': "['order']", 'object_name': 'Region'},
            'countries': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'countries'", 'symmetrical': 'False', 'to': "orm['contactisobar.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '999'}),
            'people': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['contactisobar.Person']", 'max_length': '200', 'symmetrical': 'False'})
        }
    }

    complete_apps = ['contactisobar']
