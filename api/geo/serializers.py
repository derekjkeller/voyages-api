from rest_framework import serializers
from rest_framework.fields import SerializerMethodField,IntegerField,CharField
import re
from .models import *
from drf_spectacular.utils import extend_schema_serializer, OpenApiExample
from django.core.exceptions import ObjectDoesNotExist
from drf_writable_nested.serializers import WritableNestedModelSerializer
from drf_writable_nested.mixins import UniqueFieldsMixin

class LocationTypeSerializer(UniqueFieldsMixin, serializers.ModelSerializer):
	class Meta:
		model=LocationType
		fields='__all__'
	def create(self, validated_data):
		#really smart get_or_create-like hack here
		#https://stackoverflow.com/questions/26247192/reuse-existing-object-in-django-rest-framework-nested-serializer
		try:
			# if there is already an instance in the database with the
			# given value (e.g. tag='apple'), we simply return this instance
			return LocationType.objects.get(name=validated_data['name'])
		except ObjectDoesNotExist:
			# else, we create a new tag with the given value
			return super(LocationTypeSerializer, self).create(validated_data)


class PolygonSerializer(serializers.ModelSerializer):
	class Meta:
		model=Polygon
		fields='__all__'

class LocationParentSerializer(serializers.ModelSerializer):
	class Meta:
		model=Location
		fields='__all__'

class LocationChildSerializer(serializers.ModelSerializer):
	class Meta:
		model=Location
		fields='__all__'


class LocationSerializerDeep(serializers.ModelSerializer):
	parents=LocationParentSerializer(many=False)
	children=LocationChildSerializer(many=True)
	spatial_extent=PolygonSerializer(many=False)
	location_type=LocationTypeSerializer(many=False)
	class Meta:
		model=Location
		fields='__all__'

class LocationSerializer(WritableNestedModelSerializer):
	spatial_extent=PolygonSerializer(many=False,allow_null=True)
	location_type=LocationTypeSerializer(many=False)
	class Meta:
		model=Location
		fields='__all__'