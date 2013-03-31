from tastypie.resources import ModelResource
from memopol.votes.models import VotesData


class RecommendationDataResource(ModelResource):
    class Meta:
        queryset = VotesData.objects.all()
