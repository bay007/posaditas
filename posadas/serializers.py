

from posadas.models import Posada

from rest_framework import serializers


class PosadaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Posada
        fields = "__all__"
