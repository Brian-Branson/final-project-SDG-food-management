from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Food
from .forms import FoodForm

# Home page to list food items
def index(request):
    foods = Food.objects.all()
    return render(request, 'food/index.html', {'foods': foods})

# View to add new food item
def add_food(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = FoodForm()
    return render(request, 'food/add_food.html', {'form': form})

# View to delete a food item
def delete_food(request, food_id):
    food = Food.objects.get(id=food_id)
    food.delete()
    return redirect('index')
