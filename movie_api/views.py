from rest_framework.views import APIView,status,Response
from .serializers import MovieHomeApiSerializer,MovieDetailsFetchSerializer
from .models import Movie



class TicketBookHomeView(APIView):
    '''
    Home api view
    '''
    def get(self, request):
        serializer_data = MovieHomeApiSerializer(instance=Movie.objects.all(),many=True)
        return Response(serializer_data.data,status=status.HTTP_200_OK)
    


class SpecificMovieDetails(APIView):
    '''
    Movie all details api view
    '''
    def get(self, request, id):
        try:
            serializer = MovieDetailsFetchSerializer(Movie.objects.get(id=id))
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(f"{e}",status=status.HTTP_404_NOT_FOUND)
