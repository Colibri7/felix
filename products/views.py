from math import ceil

from django.db.models import Q, Min, Max
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from products.forms import CommentModelForm
from products.models import ProductsModel, CategoryModel, ProductTagModel, BrandModel, SizeModel, GenderModel, \
    ColorsModel



class ProductListView(ListView):
    template_name = 'products.html'
    paginate_by = 9

    def get_queryset(self):
        qs = ProductsModel.objects.order_by('-pk')
        q = self.request.GET.get('q')
        cat = self.request.GET.get('cat')
        brand = self.request.GET.get('brand')
        tag = self.request.GET.get('tag')
        size = self.request.GET.get('size')
        price = self.request.GET.get('price')

        if q:
            qs = qs.filter(Q(title__icontains=q))
        if cat:
            qs = qs.filter(category__id=cat)
        if brand:
            qs = qs.filter(brand__id=brand)


        if price:
            price = price.split(';')
            price_from, price_to = price
            qs = qs.filter(real_price__gte=price_from, real_price__lte=price_to)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryModel.objects.all()
        context['tags'] = ProductTagModel.objects.all()
        context['brands'] = BrandModel.objects.all()
        context['size'] = SizeModel.objects.all()
        context['gender'] = GenderModel.objects.all()
        context['colors'] = ColorsModel.objects.all()


        max_price, min_price = ProductsModel.objects.aggregate(Max('real_price'), Min('real_price')).values()

        context['min_price'] = ceil(min_price)
        context['max_price'] = ceil(max_price)
        return context


class ProductDetailView(DetailView):
    template_name = 'product.html'
    model = ProductsModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_products'] = self.object.brand.products.exclude(pk=self.object.pk)[:8]

        return context


def add_to_cart(request, pk):
    cart = request.session.get('cart')

    if not cart:
        cart = []

    if pk in cart:
        cart.remove(pk)
    else:
        cart.append(pk)

    request.session['cart'] = cart
    return redirect(request.GET.get('next', '/'))



class CartListView(ListView):
    template_name = 'shopping-cart.html'

    def get_queryset(self):
        cart = self.request.session.get('cart', [])
        return ProductsModel.objects.filter(pk__in=cart)




class CommentCreateView(CreateView):
    form_class = CommentModelForm

    def get_success_url(self):
        return reverse('products:detail', kwargs={'pk': self.kwargs.get('pk')})

    def form_valid(self, form):
        pk = self.kwargs.get('pk')
        form.instance.product = get_object_or_404(ProductsModel, pk=pk)
        return super().form_valid(form)