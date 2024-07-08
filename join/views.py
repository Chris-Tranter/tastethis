from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Join


def join_me(request):
    """
    Renders the joinpage
    """
    join = Join.objects.all()

    return render(
        request,
        "join/join.html",
        {"join": join},
    )