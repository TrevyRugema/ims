from .models import *
from rest_framework import serializers


class JobcardSerializer( serializers.ModelSerializer):
    model=JobCard
    fields='__all__'