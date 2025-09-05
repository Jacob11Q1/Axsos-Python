# leagues/management/commands/populate_sports.py

from django.core.management.base import BaseCommand
from leagues.models import League, Team, Player

class Command(BaseCommand):
    help = "Populate the database with leagues, teams, and players"

    def handle(self, *args, **kwargs):
        # Clear previous data
        Player.objects.all().delete()
        Team.objects.all().delete()
        League.objects.all().delete()

        # Create leagues
        mlb = League.objects.create(name="Major League Baseball", sport="Baseball")
        wnba = League.objects.create(name="Women's National Basketball Association", sport="Basketball")
        nfl = League.objects.create(name="National Football League", sport="Football")
        nhl = League.objects.create(name="National Hockey League", sport="Hockey")
        nba = League.objects.create(name="National Basketball Association", sport="Basketball")

        # Create teams
        yankees = Team.objects.create(team_name="New York Yankees", location="New York", league=mlb)
        dodgers = Team.objects.create(team_name="Los Angeles Dodgers", location="Los Angeles", league=mlb)
        lynx = Team.objects.create(team_name="Minnesota Lynx", location="Minnesota", league=wnba)
        sparks = Team.objects.create(team_name="Los Angeles Sparks", location="Los Angeles", league=wnba)
        patriots = Team.objects.create(team_name="New England Patriots", location="New England", league=nfl)
        cowboys = Team.objects.create(team_name="Dallas Cowboys", location="Dallas", league=nfl)
        penguins = Team.objects.create(team_name="Pittsburgh Penguins", location="Pittsburgh", league=nhl)
        maple_leafs = Team.objects.create(team_name="Toronto Maple Leafs", location="Toronto", league=nhl)
        lakers = Team.objects.create(team_name="Los Angeles Lakers", location="Los Angeles", league=nba)
        celtics = Team.objects.create(team_name="Boston Celtics", location="Boston", league=nba)

        # Create players
        Player.objects.create(first_name="Babe", last_name="Ruth", team=yankees)
        Player.objects.create(first_name="Clayton", last_name="Kershaw", team=dodgers)
        Player.objects.create(first_name="Maya", last_name="Moore", team=lynx)
        Player.objects.create(first_name="Candace", last_name="Parker", team=sparks)
        Player.objects.create(first_name="Tom", last_name="Brady", team=patriots)
        Player.objects.create(first_name="Dak", last_name="Prescott", team=cowboys)
        Player.objects.create(first_name="Sidney", last_name="Crosby", team=penguins)
        Player.objects.create(first_name="Auston", last_name="Matthews", team=maple_leafs)
        Player.objects.create(first_name="LeBron", last_name="James", team=lakers)
        Player.objects.create(first_name="Jayson", last_name="Tatum", team=celtics)

        self.stdout.write(self.style.SUCCESS("Database populated successfully!"))
