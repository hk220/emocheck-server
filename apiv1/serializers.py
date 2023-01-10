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


class ResultModelSerializer(serializers.ModelSerializer):
  scan_time = serializers.DateTimeField(format=SCAN_TIME_DATETIME_FORMAT, input_formats=[SCAN_TIME_DATETIME_FORMAT])
  is_infected = MyChoiceField(choices=TRUE_FALSE_CHOICES)

  class Meta:
    model = Result
    fields = ['scan_time', 'hostname', 'emocheck_version', 'is_infected']


class EmotetProcessModelSerializer(serializers.ModelSerializer):
  class Meta:
    model = EmotetProcess
    fields = ['process_name', 'process_id', 'image_path', 'registry_key']
