from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render

from .forms import UserSignupForm

# Create your views here.
User = get_user_model()
from django.views.generic import ListView


class UserListView(ListView):
    model = User
    template_name = "account/user_list.html"
    paginate_by = 40


def SignUpUserView(request):
    form = UserSignupForm
    if request.method == "POST":
        form = form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(
                username=cd["phone_number"], password="12345"
            )
            user.profile.name = cd["name"]
            user.profile.family = cd["family"]
            user.profile.national_code = cd["national_code"]
            user.profile.save()
            return redirect("account:user_list")
    return render(request, "account/signup.html", {"form": form})
