from django.views.generic import DetailView, ListView

from .models import Order, OrderItem


# Create your views here.
class OrderListView(ListView):
    model = Order
    template_name = "order/order_list.html"


class OrderDetailView(DetailView):
    model = Order
    slug_field = "id"
    slug_url_kwarg = "id"
    template_name = "order/order_detail.html"


class OrderItemView(ListView):
    model = OrderItem
    template_name = "order/order_item_list.html"


class OrderItemDetailView(DetailView):
    model = OrderItem
    slug_field = "id"
    slug_url_kwarg = "id"
    template_name = "order/order_item_detail.html"
