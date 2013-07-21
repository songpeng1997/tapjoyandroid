# Create your views here.
from django.shortcuts import render, get_object_or_404
from apps.models import Category, SubCategory, App

def category(request, category_id):
    """ sub category list in this category """
    category = get_object_or_404(Category, pk=category_id)
    subcategory_list = category.subcategory_set.all()
    return render(request, 'apps/subcategory_list.html',  {'category':category, 'subcategory_list':subcategory_list})

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
    