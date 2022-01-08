from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render, get_object_or_404

from .forms import UserSignupForm, EditProfileForm

# Create your views here.
User = get_user_model()
from django.views.generic import ListView


class UserListView(ListView):
    model = User
    template_name = "account/user_list.html"
    paginate_by = 40


def delete_user(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    return redirect("account:user_list")


def SignUpUserView(request):
    form = UserSignupForm
    if request.method == "POST":
        form = UserSignupForm(request.POST)
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





def UserUpdateView(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=user.profile)
        if form.is_valid():
            form.save()
            user.username = form.cleaned_data['phone_number']
            user.save()
            return redirect("account:user_list")
    else:
        form = EditProfileForm(instance=user.profile, initial={'phone_number': request.user.username})
    return render(request, 'account/edit_profile.html', {'form': form})
