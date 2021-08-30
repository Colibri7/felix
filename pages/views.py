from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, CreateView
from django.conf import settings
from pages.forms import ContactForm
from pages.models import HomeModel
from products.models import CategoryModel, ProductTagModel, BrandModel, ProductsModel



class ContactCreateView(CreateView):
    template_name = 'contact-us.html'
    form_class = ContactForm

    def get_success_url(self):
        return reverse('pages:contact')

    def form_valid(self, form):
        obj = form.save()
        text = f"""Name: {obj.name}\nPhone:{obj.phone}\nMessage: {obj.text}"""
        send_mail(
            'Notification',
            text,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
        )

        return redirect(self.success_url)



class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['home'] = HomeModel.objects.all()
        context['categories'] = CategoryModel.objects.all()
        context['tags'] = ProductTagModel.objects.all()
        context['brands'] = BrandModel.objects.all()
        return context


class WishlistListView(LoginRequiredMixin, ListView):
    template_name = 'wishlist.html'
    paginate_by = 9

    def get_queryset(self):
        return self.request.user.wishlist.all()


@login_required
def add_to_wishlist(request, pk):
    product = get_object_or_404(ProductsModel, pk=pk)
    user = request.user

    if user in product.wishlist.all():
        product.wishlist.remove(user)
    else:
        product.wishlist.add(user)

    return redirect(request.GET.get('next', '/'))
