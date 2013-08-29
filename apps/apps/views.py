# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from apps.models import Category, SubCategory, App, CarouselApp, AppDownload
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import F
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import json


def app_pagination(request, apps, page): 
    paginator = Paginator(apps, 5) # Show 5 apps per page
    try:
        apps_list = paginator.page(page)
    except PageNotAnInteger:
        apps_list = paginator.page(1)
    except EmptyPage:
        #apps_list = paginator.page(paginator.num_pages)
        apps_list = None
    return render(request, 'apps/apps_page.html',{'apps_list':apps_list})  

def category_app_list(request, category_id, page):
    category = get_object_or_404(Category, pk=category_id)
    subcategory_list = category.subcategory_set.all()
    apps = App.objects.filter(sub_catg__in=subcategory_list).filter(recomm_flag_on_catg=True).order_by('recomm_catg_date')   
    return app_pagination(request, apps, page)

def category(request, category_id):
    """ sub category list in this category """
    category = get_object_or_404(Category, pk=category_id)
    subcategory_list = category.subcategory_set.all()
    return render(request, 'apps/subcategory_list.html',  {'category':category, 
                                                           'subcategory_list':subcategory_list})

def subcategory_app_list(request, subcategory_id, page):
    sub_category = get_object_or_404(SubCategory, pk=subcategory_id)
    apps = sub_category.app_set.all().order_by('pub_date')
    return app_pagination(request, apps, page)

def sub_category(request, subcategory_id):
    """ app list in the sub category """
    sub_category = get_object_or_404(SubCategory, pk=subcategory_id)
    return render(request, 'apps/apps_list.html', {'sub_category':sub_category})


def app_detail(request, app_id):
    app = get_object_or_404(App, app_id=app_id)
    return render(request, 'apps/app_detail.html', {'app':app})


def search(request):
    """ search page """
    if request.method == 'POST':
        query=request.POST.get('query',None)
        r=App.search.query(query)
        apps_list=list(r)
        context={'apps_list':apps_list,'query':query,'search_meta':r._sphinx}
    else:
        apps_list=list()
        context={'apps_list':apps_list,}
    return render(request, 'apps/apps_search.html',context)  



def home_recomm_list(request, page):
    apps = App.objects.filter(recomm_flag_on_index=True).order_by('recomm_index_date')
    return app_pagination(request, apps, page)

def home(request):
    apps_list = CarouselApp.objects.all()
    return render(request, 'apps/apps_index.html', {'apps_list':apps_list})




def download(request):
    
    if request.method != 'POST' or 'app_id' not in request.POST:
        raise Http404('Parameters error')

    app_id = request.POST['app_id']
    app = get_object_or_404(App, app_id=app_id)
    if not request.session.get(app_id, False):
        # new download
        try:
            appdl = app.appdownload
            appdl.count = F('count') + 1
        except ObjectDoesNotExist:
            appdl = AppDownload(app=app)
            appdl.count = 1
        appdl.save()
        json_data = json.dumps({"result":0})
        request.session[app_id] = True

    else:
        # already downloaded
        json_data = json.dumps({"result":1})   
    # json data is just a JSON string now. 
    return HttpResponse(json_data, mimetype="application/json")

    