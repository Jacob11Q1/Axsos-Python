from django.shortcuts import render
from sports_orm.models import League, Team, Player

# Create your views here.

def index(request):
    context = {
        # Leagues Queries
        "baseball_leagues": League.objects.filter(sport__icontains="Baseball"),
        "womens_leagues": League.objects.filter(name__icontains="Women"),
        "hockey_leagues": League.objects.filter(sport__icontains="Hockey"),
        "non_football_leagues": League.objects.exclude(sport__icontains="Football"),
        "conference_leagues": League.objects.filter(name__icontains="Conference"),
        "atlantic_leagues": League.objects.filter(name__icontains="Atlantic"),

        # Teams Queries
        "dallas_teams": Team.objects.filter(location__icontains="Dallas"),
        "raptors_teams": Team.objects.filter(team_name__icontains="Raptors"),
        "city_teams": Team.objects.filter(location__icontains="City"),
        "t_teams": Team.objects.filter(team_name__startswith="T"),
        "teams_by_location": Team.objects.all().order_by("location"),
        "teams_by_name_desc": Team.objects.all().order_by("-team_name"),

        # Players Queries
        "cooper_players": Player.objects.filter(last_name="Cooper"),
        "joshua_players": Player.objects.filter(first_name="Joshua"),
        "cooper_not_joshua": Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua"),
        "alex_or_wyatt": Player.objects.filter(first_name__in=["Alexander", "Wyatt"]),
    }

    return render(request, "leagues/index.html", context)