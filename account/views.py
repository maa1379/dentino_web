from django.contrib.auth import get_user_model

# Create your views here.
user = get_user_model()
from django.views.generic import ListView


class UserListView(ListView):
    model = user
    template_name = "account/user_list.html"
    paginate_by = 40
