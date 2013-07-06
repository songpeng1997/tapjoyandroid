# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'apps_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('catg_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'apps', ['Category'])

        # Adding model 'SubCategory'
        db.create_table(u'apps_subcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('catg', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['apps.Category'])),
            ('sub_catg_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'apps', ['SubCategory'])

        # Adding model 'App'
        db.create_table(u'apps_app', (
            ('id', self.gf('django.db.models.fields.CharField')(default=('00000000-0000-0000-0000-000000000000'), max_length=36, primary_key=True)),
            ('sub_catg', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['apps.SubCategory'])),
            ('app_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=1000)),
            ('apk', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('icon', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('img1', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('img2', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('img3', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('img4', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('version', self.gf('django.db.models.fields.CharField')(default='\xe6\x9c\xaa\xe7\x9f\xa5', max_length=32)),
            ('size', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('vendor_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'apps', ['App'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'apps_category')

        # Deleting model 'SubCategory'
        db.delete_table(u'apps_subcategory')

        # Deleting model 'App'
        db.delete_table(u'apps_app')


    models = {
        u'apps.app': {
            'Meta': {'object_name': 'App'},
            'apk': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'app_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'00000000-0000-0000-0000-000000000000'", 'max_length': '36', 'primary_key': 'True'}),
            'img1': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'img2': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'img3': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'img4': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'size': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sub_catg': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['apps.SubCategory']"}),
            'vendor_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'\\xe6\\x9c\\xaa\\xe7\\x9f\\xa5'", 'max_length': '32'})
        },
        u'apps.category': {
            'Meta': {'object_name': 'Category'},
            'catg_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'apps.subcategory': {
            'Meta': {'object_name': 'SubCategory'},
            'catg': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['apps.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sub_catg_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['apps']
