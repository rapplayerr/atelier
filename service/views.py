from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Service
# from .forms import ArticleForm
from django.views.generic import DetailView, UpdateView, DeleteView

def services_list(request):    
    categories = Category.objects.filter(is_visible = True)
    context = {
        'title': 'Наши услуги',
        'categories': categories,
    }
    return render(request, 'service/services_list.html',context)
def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug, is_visible = True)
    services = category.services.filter(is_visible = True)
    context = {
        'title': category.name,
        'category': category,
        'services': services,
    }
    return render(request, 'service/category_detail.html', context)

def service_detail(request, category_slug, service_slug):
    category = get_object_or_404(Category, slug=category_slug)
    service = get_object_or_404(Service, category=category, slug=service_slug)
    
    return render(request, 'service/service_detail.html', {
        'category': category,
        'service': service,
    })
# class Dynamicpage(DetailView):
#     model = Article
#     template_name = 'service/dynamicpage.html'
#     context_object_name = 'article'

    
