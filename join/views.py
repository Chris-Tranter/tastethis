from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Join
from .forms import JoinForm


def join_me(request):
    """
    Renders the joinpage
    """
    if request.method == "POST":
        join_form = JoinForm(data=request.POST)
        if join_form.is_valid():
            join_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Thanks for requesting to join the team, check your emails soon.",
            )

    join = Join.objects.all()
    join_form = JoinForm()

    return render(
        request,
        "join/join.html",
        {"join": join, "join_form": join_form},
    )
