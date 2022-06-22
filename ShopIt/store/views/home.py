from django.shortcuts import render
from store.models.product import Product
from store.models.category import Category


def index(request):
    pr = None;
    cat = Category.get_all_category()
    cat_id = request.GET.get('category')
    if cat_id:
        pr = Product.get_all_product_by_id(cat_id)
    else:
        pr = Product.get_all_products()
    data = {}
    data['products'] = pr
    data['Category'] = cat

    return render(request, "index.html", data)