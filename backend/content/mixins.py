from django.shortcuts import get_object_or_404


class CheckUserObject():
    def dispatch(self, request, *args, **kwargs):
        """Проверка на авторство."""
        get_object_or_404(
            self.model,
            pk=kwargs['pk'],
            user=request.user
        )
        return super().dispatch(request, *args, **kwargs)
