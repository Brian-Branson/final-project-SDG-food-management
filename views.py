from django.shortcuts import render, redirect
from .models import FoodItem
from .forms import FoodItemForm

def food_list(request):
    food_items = FoodItem.objects.all().order_by('-expiry_date')
    return render(request, 'food_manager/food_list.html', {'food_items': food_items})

def add_food(request):
    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('food_list')
    else:
        form = FoodItemForm()
    return render(request, 'food_manager/add_food.html', {'form': form})

def check_expired(request):
    expired_items = FoodItem.objects.filter(expiry_date__lt=datetime.date.today())
    return render(request, 'food_manager/expired_items.html', {'expired_items': expired_items})

def reduce_food_waste(request):
    FoodItem.objects.filter(expiry_date__lt=datetime.date.today()).delete()
    return redirect('food_list')
