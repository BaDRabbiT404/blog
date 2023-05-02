from django.shortcuts import render


def about(request):
    """Выводит страницу О проекте."""
    template = 'pages/about.html'
    return render(request, template)


def rules(request):
    """Выводит страницу Наши правила."""
    template = 'pages/rules.html'
    return render(request, template)
