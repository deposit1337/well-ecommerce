from django.shortcuts import render

positions = [
    {'id': 1, 'name': 'Резцы', 'subname_1': 'THE FIRST NAME', 'subname_2': 'THE SECOND NAME', 'quan_1': 'FIRST QUAN', 'quan_2': 'SECOND QUAN'},
    {'id': 2, 'name': 'Зубья', 'subname_1': 'THE FIRST NAME', 'subname_2': 'THE SECOND NAME', 'quan_1': 'FIRST QUAN', 'quan_2': 'SECOND QUAN'},
    {'id': 3, 'name': 'АВОЫШЛАОлЫВОАЛОЫА', 'subname_1': 'THE FIRST NAME', 'subname_2': 'THE SECOND NAME', 'quan_1': 'FIRST QUAN', 'quan_2': 'SECOND QUAN'},
{'id': 4, 'name': 'Гусеницы', 'subname_1': 'THE FIRST NAME', 'subname_2': 'THE SECOND NAME', 'quan_1': 'FIRST QUAN', 'quan_2': 'SECOND QUAN'},
{'id': 5, 'name': 'Пружины', 'subname_1': 'THE FIRST NAME', 'subname_2': 'THE SECOND NAME', 'quan_1': 'FIRST QUAN', 'quan_2': 'SECOND QUAN'},
{'id': 6, 'name': 'Пильные диски', 'subname_1': 'THE FIRST NAME', 'subname_2': 'THE SECOND NAME', 'quan_1': 'FIRST QUAN', 'quan_2': 'SECOND QUAN'},
]






def home(request):
    context = {'positions': positions}
    return render(request, 'index.html',context)

def catalog(request,pk):
    position = None
    for i in positions:
        if i['name'] == str(pk):
            position = i
    context = {'position': position}
    return render(request,'catalog.html',context)

def item_page(request):
    return render(request, 'item-page.html')