from django.shortcuts import render

# from .models import


#
# positions = [
#     {'id': 1, 'name': 'Резцы', 'subname_1': 'THE FIRST NAME', 'subname_2': 'THE SECOND NAME', 'quan_1': 'FIRST QUAN', 'quan_2': 'SECOND QUAN'},
#     {'id': 2, 'name': 'Зубья', 'subname_1': 'THE FIRST NAME', 'subname_2': 'THE SECOND NAME', 'quan_1': 'FIRST QUAN', 'quan_2': 'SECOND QUAN'},
#     {'id': 3, 'name': 'АВОЫШЛАОлЫВОАЛОЫА', 'subname_1': 'THE FIRST NAME', 'subname_2': 'THE SECOND NAME', 'quan_1': 'FIRST QUAN', 'quan_2': 'SECOND QUAN'},
# {'id': 4, 'name': 'Гусеницы', 'subname_1': 'THE FIRST NAME', 'subname_2': 'THE SECOND NAME', 'quan_1': 'FIRST QUAN', 'quan_2': 'SECOND QUAN'},
# {'id': 5, 'name': 'Пружины', 'subname_1': 'THE FIRST NAME', 'subname_2': 'THE SECOND NAME', 'quan_1': 'FIRST QUAN', 'quan_2': 'SECOND QUAN'},
# {'id': 6, 'name': 'Пильные диски', 'subname_1': 'THE FIRST NAME', 'subname_2': 'THE SECOND NAME', 'quan_1': 'FIRST QUAN', 'quan_2': 'SECOND QUAN'},
# ]

from .models import Category,Product



def home(request):
    categories_red = Category.objects.all()[:3]
    categories_grey = Category.objects.all()[3:6]

    return render(request, 'index.html',{'categories_red': categories_red,'categories_grey':categories_grey})

# def products(request):
#     products = Product.objects.all()
#     return render(request,'catalog.html',{'products':products})


from django.http import Http404

from django.utils.translation import gettext as _
from django.shortcuts import get_object_or_404

def category_products(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'catalog.html', {'category': category, 'products': products})