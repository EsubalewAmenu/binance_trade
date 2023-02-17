import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .common import exchangeInfoApiUrl
from ..models import Symbols

class UpdateSymbolsAPIView(ListAPIView):

    queryset = Symbols.objects.all()
    serializer_class = SymbolsListSerializer
    permission_classes = [AllowAny]
    pagination_class = DefaultLimitOffsetPagination

    def get_queryset(self):     
        last_updated_symbol =  self.queryset.filter(symbol__endswith='busd').order_by('-updated_at').first()

        # base_url = 'http://example.com/'  # Replace with your base URL
        # url = f'{base_url}{api_endpoint}'
        response = requests.get(exchangeInfoApiUrl)
        if response.status_code == 200:
            data = response.json()
            return Response(data, status=200)
        else:
            return Response({"error": f"Request failed with status code {response.status_code}"}, status=response.status_code)

            
        return self.queryset.filter(user=self.request.user)


# class CreateUpdateSymbolsAPIView(APIView):
#     queryset = Symbols.objects.all()
#     lookup_url_kwarg = "subscriber_slug"
#     serializer_class = SymbolsCreateUpdateSerializer
#     permission_classes = [
#         IsAuthenticated,
#     ]

#     def get(self, request):
#         # base_url = 'http://example.com/'  # Replace with your base URL
#         # url = f'{base_url}{api_endpoint}'

#         response = requests.get(exchangeInfoApiUrl)
#         if response.status_code == 200:
#             data = response.json()
#             return Response(data, status=200)
#         else:
#             return Response({"error": f"Request failed with status code {response.status_code}"}, status=response.status_code)
