# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from apps.models import Category, SubCategory, App, CarouselApp, AppDownload
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import F

import json

def category(request, category_id):
    """ sub category list in this category """
    category = get_object_or_404(Category, pk=category_id)
    subcategory_list = category.subcategory_set.all()
    re_apps_list = App.objects.filter(sub_catg__in=subcategory_list).filter(recomm_flag_on_catg=True)[:5]
    return render(request, 'apps/subcategory_list.html',  {'category':category, 
                                                           'subcategory_list':subcategory_list, 
                                                           're_apps_list':re_apps_list})


def sub_category(request, subcategory_id):
    """ app list in the sub category """
    sub_category = get_object_or_404(SubCategory, pk=subcategory_id)
    apps_list = sub_category.app_set.all()[:5]

    #output = ', '.join([p.question for p in latest_poll_list])
    return render(request, 'apps/apps_list.html', {'sub_category':sub_category, 'apps_list':apps_list})

def app_detail(request, app_id):
    app = get_object_or_404(App, app_id=app_id)
    return render(request, 'apps/app_detail.html', {'app':app})


def search(request):
    if request.method == 'POST':
        query=request.POST.get('query',None)
        r=App.search.query(query)
        apps_list=list(r)[:5]
        context={'apps_list':apps_list,'query':query,'search_meta':r._sphinx}
    else:
        apps_list=list()
        context={'apps_list':apps_list,}
    return render(request, 'apps/apps_search.html',context)  


def home(request):
    apps_list = CarouselApp.objects.all()
    re_apps_list = App.objects.filter(recomm_flag_on_index=True)[:5]
    return render(request, 'apps/apps_index.html', {'apps_list':apps_list, 're_apps_list':re_apps_list})


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

    