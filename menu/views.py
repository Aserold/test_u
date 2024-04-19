from django.db.models import Prefetch
from rest_framework.generics import ListAPIView

from .models import FoodCategory, Food
from .serializers import FoodListSerializer


class GetOrders(ListAPIView):
    serializer_class = FoodListSerializer

    def get_queryset(self):
        published_foods_prefetch = Prefetch(
            'food', queryset=Food.objects.filter(is_publish=True)
            )

        queryset = FoodCategory.objects.filter(
            food__is_publish=True
        ).prefetch_related(published_foods_prefetch).distinct().order_by('id')

        return queryset
