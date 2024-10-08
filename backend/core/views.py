from django.shortcuts import render


def page_not_found(request, exception):
    """Ошибка 404."""
    return render(
        request,
        'core/404.html',
        status=404
    )

def page_error(request):
    """Ошибка 500."""
    return render(
        request,
        'core/500.html',
        status=404
    )


def csrf_failure(request, reason=''):
    """Ошибка 403."""
    return render(
        request,
        'core/403csrf.html',
        status=403
    )
