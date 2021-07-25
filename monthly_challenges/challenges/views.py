from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse


monthly_challenge = {
    "january": "I am january",
    "february": "I am Feb",
    "march": "I am march",
    "april": "I am april",
    "december": None,
}


def index(request):
    list_items = ""
    months = list(monthly_challenge.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })
    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f"<li> <a href='{month_path}'>{capitalized_month}</a></li>"

    # response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenges_by_number(request, month):
    months = list(monthly_challenge.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse(
        "month-challenge", args=[redirect_month])  # challenge/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenge[month]
        return render(request, "challenges/challenges.html", {
            "text": challenge_text,
            "current_month": month,
        })
        # return HttpResponse(response_data)
    except:
        raise Http404()
