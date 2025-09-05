import json
from django.shortcuts import render
from .models import League, Team, Player
from django.db.models import Q

def index(request):
    querysets = [
        ("All Baseball Leagues", League.objects.filter(sport__icontains="Baseball")),
        ("All Women's Leagues", League.objects.filter(name__icontains="Women")),
        ("All Hockey Leagues", League.objects.filter(sport__icontains="Hockey")),
        ("Leagues NOT Football", League.objects.exclude(sport__icontains="Football")),
        ("Leagues called Conferences", League.objects.filter(name__icontains="Conference")),
        ("Leagues in Atlantic Region", League.objects.filter(name__icontains="Atlantic")),
        ("Teams in Dallas", Team.objects.filter(location__icontains="Dallas")),
        ("Teams named Raptors", Team.objects.filter(team_name__icontains="Raptors")),
        ("Teams with 'City' in location", Team.objects.filter(location__icontains="City")),
        ("Teams starting with 'T'", Team.objects.filter(team_name__startswith="T")),
        ("Teams by Location (A-Z)", Team.objects.order_by("location")),
        ("Teams by Name (Z-A)", Team.objects.order_by("-team_name")),
        ("Players with last name Cooper", Player.objects.filter(last_name__icontains="Cooper")),
        ("Players named Joshua", Player.objects.filter(first_name__icontains="Joshua")),
        ("Players Cooper NOT Joshua", Player.objects.filter(last_name__icontains="Cooper").exclude(first_name__icontains="Joshua")),
        ("Players Alexander or Wyatt", Player.objects.filter(Q(first_name__icontains="Alexander") | Q(first_name__icontains="Wyatt"))),
    ]

    # Prepare JSON data for charts
    chart_data = []
    for title, qs in querysets:
        labels = [getattr(obj, 'team_name', getattr(obj, 'first_name', getattr(obj, 'name', 'Unknown'))) for obj in qs]
        data = [5 + i for i in range(len(qs))]  # Example dummy stats
        chart_data.append({"title": title, "labels": labels, "data": data})

    return render(request, "leagues/index.html", {"querysets": querysets, "chart_data": json.dumps(chart_data)})
