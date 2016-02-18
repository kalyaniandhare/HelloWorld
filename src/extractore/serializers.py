from extractore.models import Extractore, StoreData
from rest_framework import serializers


class StoreDataSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = StoreData
        fields = ('username','useremailid', 'email_from', 'email_to','date','subject','filename','filedata')
