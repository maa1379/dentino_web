class DoctorMixins:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            fields = []
