from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.decorators import action

from .models import *
from .serializers import *


class TeamListView(APIView):
    @staticmethod
    def get(request):
        teams = Team.objects.all().order_by('name')
        instances = TeamSerializer(teams, many=True).data
        return Response(instances)


class PilotListView(APIView):
    @staticmethod
    def get(request):
        pilots = Pilot.objects.filter(is_main_pilot=True).\
            order_by('league', '-total_score', 'best_race_finish', 'highest_grid_position')
        instances = PilotSerializer(pilots, many=True).data
        return Response(instances)


class AllPilotListView(APIView):
    @staticmethod
    def get(request):
        pilots = Pilot.objects.all().order_by('league')
        instances = PilotSerializer(pilots, many=True).data
        return Response(instances)


class TeamDetailView(APIView):
    @staticmethod
    def get(request, url_name):
        teams = Team.objects.get(url_name=url_name)
        instances = TeamSerializer(teams).data
        return Response(instances)


class RaceListView(APIView):
    @staticmethod
    def get(request):
        race = Race.objects.all().order_by('place_in_calendar')
        instances = RaceSerializer(race, many=True).data
        return Response(instances)


class RaceDetailView(APIView):
    @staticmethod
    def get(request, country):
        race = Race.objects.get(country=country)
        instances = RaceSerializer(race).data
        return Response(instances)


class ResultListView(APIView):
    @staticmethod
    def post(request: Request):
        results = request.data.get('results', None)
        for result in results:
            if result.pilot_id:
                Result.objects.create(league=result.league, race_id=result.race_id, pilot_id=result.pilot_id,
                                      team_id=result.team_id, race_position=result.race_position,
                                      race_table_position=result.race_table_position,
                                      qualifying_position=result.qualifying_position, best_lap=result.best_lap,
                                      is_race_best_lap=result.is_race_best_lap,
                                      is_result_of_reserve_pilot=result.is_result_of_reserve_pilot)
        return Response(200)
