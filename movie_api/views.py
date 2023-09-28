from rest_framework.views import APIView,status,Response
from .serializers import MovieHomeApiSerializer,MovieDetailsFetchSerializer
from .models import Movie



class TicketBookHomeView(APIView):
    
    def get(self, request):
        serializer_data = MovieHomeApiSerializer(instance=Movie.objects.all(),many=True)
        return Response(serializer_data.data,status=status.HTTP_200_OK)
    


class SpecificMovieDetails(APIView):
    
    def get(self, request, id):
        try:
            serializer = MovieDetailsFetchSerializer(Movie.objects.get(id=id),many=False)
        except Exception as e:
            return Response(f"{e}",status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.data,status=status.HTTP_200_OK)