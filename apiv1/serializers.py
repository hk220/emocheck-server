from rest_framework import serializers

from emocheck.models import Result, EmotetProcess


SCAN_TIME_DATETIME_FORMAT="%Y-%m-%d %H:%M:%S"

class ResultSerializer(serializers.Serializer):
  scan_time = serializers.DateTimeField(format=SCAN_TIME_DATETIME_FORMAT, input_formats=[SCAN_TIME_DATETIME_FORMAT])
  hostname = serializers.CharField(max_length=255)
  emocheck_version = serializers.CharField(max_length=255)
  is_infected = serializers.ChoiceField(choices=[(True, 'yes'),(False, 'no')])

  def create(self, validated_data):

    return Result.objects.create(**validated_data)

  def update(self, instance, validated_data):
    instance.scan_time = validated_data.get('scan_time', instance.scan_time)
    instance.hostname = validated_data.get('hostname', instance.hostname)
    instance.emocheck_version = validated_data.get('emocheck_version', instance.emocheck_version)
    instance.is_infected = validated_data.get('is_infected', instance.is_infected)
    instance.save()
    return instance


class ResultModelSerializer(serializers.ModelSerializer):
  class Meta:
    model = Result
    fields = ['scan_time', 'hostname', 'emocheck_version', 'is_infected']

  

class EmotetProcessModelSerializer(serializers.ModelSerializer):
  class Meta:
    model = EmotetProcess
    fields = ['process_name', 'process_id', 'image_path', 'registry_key']
