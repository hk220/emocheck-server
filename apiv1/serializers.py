from rest_framework import serializers

from emocheck.models import Result, EmotetProcess


TRUE_FALSE_CHOICES = (
    (True, 'yes'),
    (False, 'no')
)

SCAN_TIME_DATETIME_FORMAT="%Y-%m-%d %H:%M:%S"


# https://stackoverflow.com/questions/34534239/return-display-name-in-choicefield
class MyChoiceField(serializers.ChoiceField):

  def to_representation(self, value):
    if value not in self.choices.keys():
      self.fail('invalid_choice', input=value)
    else:
      return self.choices[value]

  def to_internal_value(self, data):
    for key, value in self.choices.items():
      if value == data:
        return key
    self.fail('invalid_choice', input=data)


class MyIntegerField(serializers.IntegerField):

  def to_representation(self, value):
    return str(super().to_representation(value))


class EmotetProcessModelSerializer(serializers.ModelSerializer):
  process_id = MyIntegerField()
  
  class Meta:
    model = EmotetProcess
    fields = ['process_name', 'process_id', 'image_path', 'registry_key']


class ResultModelSerializer(serializers.ModelSerializer):
  scan_time = serializers.DateTimeField(format=SCAN_TIME_DATETIME_FORMAT, input_formats=[SCAN_TIME_DATETIME_FORMAT])
  is_infected = MyChoiceField(choices=TRUE_FALSE_CHOICES)
  emotet_processes = EmotetProcessModelSerializer(many=True)

  class Meta:
    model = Result
    fields = ['scan_time', 'hostname', 'emocheck_version', 'is_infected', 'emotet_processes']

  def create(self, validated_data):
    if 'emotet_processes' in validated_data.keys():
      emotet_processes_data = validated_data.pop('emotet_processes')
      result = Result.objects.create(**validated_data)
      for emotet_process_data in emotet_processes_data:
        EmotetProcess.objects.create(result=result, **emotet_process_data)
      return result
    else:
      return Result.objects.create(**validated_data)
