# -*- encoding: utf-8 -*-

import uuid,os

from django.db import models
from djangosphinx.models import SphinxSearch
from PIL import Image

# Create your models here.

class Category(models.Model):
    catg_name = models.CharField('应用分类', max_length=100)
    #pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.catg_name

class SubCategory(models.Model):
    catg = models.ForeignKey(Category)
    sub_catg_name = models.CharField('应用二级分类', max_length=100)
    img = models.ImageField(upload_to=lambda instance, filename: '/'.join(['subcategory_meta', str(uuid.uuid1()) + '_' + filename]))

    #pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.sub_catg_name


def apk_file_name(instance, filename):
    return '/'.join(['apps_meta', str(uuid.uuid1()), filename])

def meta_file_name(instance, filename):
    folder = instance.apk.url.split(os.path.sep)[-2]
    return '/'.join(['apps_meta', folder, filename]) 

class App(models.Model):
    app_id = models.CharField(default = uuid.uuid1, max_length = 36, editable = False)
    sub_catg = models.ForeignKey(SubCategory)
    app_name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    apk = models.FileField(upload_to=apk_file_name)
    icon = models.ImageField(upload_to = meta_file_name)
    img1 = models.ImageField(upload_to = meta_file_name)
    img2 = models.ImageField(upload_to = meta_file_name)
    img3 = models.ImageField(upload_to = meta_file_name)
    img4 = models.ImageField(upload_to = meta_file_name)
    version = models.CharField(max_length=32, default = '未知')
    size = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')
    active = models.BooleanField('Live', default=False)

    APP_TYPE_CHOICES = (
    ('0', '免费'),
    ('1', '试玩转激活'),
    ('2', '道具收费'),
    ('3', '付费'),
    )
     
    app_type = models.SmallIntegerField(default=1, choices = APP_TYPE_CHOICES )

    vendor_name = models.CharField(max_length=200)

    search=SphinxSearch(index='sphinx_appdetail')

    def save(self, *args, **kwargs):
       
        super(App, self).save()
        
        #icon 100*100
        filename = str(self.icon.path)
        img = Image.open(filename)
        pw, ph = img.size
        if pw != 100 or ph != 100:
            img = img.resize((100, 100), Image.ANTIALIAS)
            img.save(filename)
        
        #preview 160*240
        for i in range(1, 5): 
            filename = str(eval('self.img' + str(i) + '.path'))
            img = Image.open(filename)
            pw, ph = img.size
            change_flag = False
            if pw > ph:
                img = img.rotate(270);
                pw, ph = img.size
                change_flag = True

            if pw != 160 or ph != 240 :
                img = img.resize((160, 240), Image.ANTIALIAS)
                change_flag = True

            if change_flag:
                img.save(filename)   
           

    def __unicode__(self):
        return self.app_name

class AppDownload(models.Model):
    app = models.OneToOneField(App, primary_key=True)
    count = models.IntegerField(default = 0)
    def __unicode__(self):
        return self.app.app_name

class CarouselApp(models.Model):
    app = models.OneToOneField(App, primary_key=True)
    description = models.TextField(max_length=1000)
    img = models.ImageField(upload_to=lambda instance, filename: '/'.join(['carousel_app_meta', str(uuid.uuid1()) + '_' + filename]))
    def __unicode__(self):
        return self.app.app_name
    

    

