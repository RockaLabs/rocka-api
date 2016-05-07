from domain.models import Rocker

from rest_framework import serializers


class RockerSerializer(serializers.ModelSerializer):

	fullname = serializers.SerializerMethodField('get_user_fullname')

	class Meta:
		model = Rocker
		fields = ('user','about', 'fullname')

	def get_user_fullname(self, instance):
		return instance.user.first_name + ' ' + instance.user.last_name
