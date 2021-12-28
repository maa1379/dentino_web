from django.shortcuts import redirect


class SuperUserMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super(SuperUserMixin, self).dispatch(request, *args, **kwargs)
        else:
            return redirect("config:panel")
