from django.shortcuts import render
from django.db.models import Count
from mailings.models import Mailing, Client
from blog.models import BlogPost
from django.core.cache import cache


def home(request):
    total_mailings = cache.get_or_set(
        "total_mailings", Mailing.objects.count(), 60 * 15
    )
    active_mailings = cache.get_or_set(
        "active_mailings", Mailing.objects.filter(is_active=True).count(), 60 * 15
    )
    unique_clients = cache.get_or_set(
        "unique_clients",
        Client.objects.aggregate(count=Count("phone_number", distinct=True))["count"],
        60 * 15,
    )
    random_posts = cache.get_or_set(
        "random_posts", BlogPost.objects.order_by("?")[:3], 60 * 15
    )

    context = {
        "total_mailings": total_mailings,
        "active_mailings": active_mailings,
        "unique_clients": unique_clients,
        "random_posts": random_posts,
    }
    return render(request, "home.html", context)
