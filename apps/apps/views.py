# Create your views here.
from django.shortcuts import render, get_object_or_404
from apps.models import Category, SubCategory, App

def apps_list(request):
    """ Default view for the root """
    return render(request, 'apps/apps_list.html')

def sub_category(request, subcategory_id):
    """ list sub category """
    sub_category = get_object_or_404(SubCategory, pk=subcategory_id)
    apps_list = sub_category.app_set.all()[:5]

    #output = ', '.join([p.question for p in latest_poll_list])
    return render(request, 'apps/apps_list.html', {'sub_category':sub_category, 'apps_list':apps_list})

def app_detail(request, app_id):
    app = get_object_or_404(App, pk=app_id)
    return render(request, 'apps/app_detail.html', {'app':app})
    