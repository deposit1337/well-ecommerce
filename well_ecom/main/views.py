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






def home(request):
    return render(request, 'index.html')

