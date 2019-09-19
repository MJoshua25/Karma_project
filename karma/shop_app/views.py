from django.shortcuts import render

# Create your views here.
# Create your views here.
def home_page(request):
    return render(request, "pages/index.html")

# Create your views here.
def category(request):
    return render(request, "pages/shop/category.html")