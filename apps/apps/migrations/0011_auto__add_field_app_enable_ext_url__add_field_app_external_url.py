# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'App.enable_ext_url'
        db.add_column(u'apps_app', 'enable_ext_url',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'App.external_url'
        db.add_column(u'apps_app', 'external_url',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'App.enable_ext_url'
        db.delete_column(u'apps_app', 'enable_ext_url')

        # Deleting field 'App.external_url'
        db.delete_column(u'apps_app', 'external_url')


    models = {
        u'apps.app': {
            'Meta': {'object_name': 'App'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'apk': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'app_id': ('django.db.models.fields.CharField', [], {'default': "'4fe6bd28-6597-11e3-ae12-406c8f1fb6eb'", 'max_length': '36'}),
            'app_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'app_type': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'enable_ext_url': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'external_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img1': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'img2': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'img3': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'img4': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'recomm_catg_date': ('django.db.models.fields.DateTimeField', [], {}),
            'recomm_flag_on_catg': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'recomm_flag_on_index': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'recomm_index_date': ('django.db.models.fields.DateTimeField', [], {}),
            'size': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sub_catg': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['apps.SubCategory']"}),
            'vendor_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'\\xe6\\x9c\\xaa\\xe7\\x9f\\xa5'", 'max_length': '32'})
        },
        u'apps.appdownload': {
            'Meta': {'object_name': 'AppDownload'},
            'app': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['apps.App']", 'unique': 'True', 'primary_key': 'True'}),
            'count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'apps.carouselapp': {
            'Meta': {'object_name': 'CarouselApp'},
            'app': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['apps.App']", 'unique': 'True', 'primary_key': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
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
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'sub_catg_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['apps']