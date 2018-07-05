from rest_framework import serializers
from .models import Data

class CommentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Data
        fields = ('data')