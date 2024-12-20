from django.shortcuts import render



DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
def recipes_view(request):
    recipe_name = request.GET.get('recipe_name')
    amount = request.GET.get('amount', 1)
   
    recipe = DATA[recipe_name]
    
    for i in recipe.items():
        ing_amount = i[1] * int(amount)
        recipe [f'{i[0]}'] = ing_amount
    
    context = {
        'recipe' : recipe
    } 
           

    return render(request, 'calculator/index.html', context)