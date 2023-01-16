from rest_framework import serializers
from API.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=['name','email','DOB','State','location','pimage','gender','rdoc']