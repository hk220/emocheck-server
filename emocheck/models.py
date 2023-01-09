from django.db import models


class Result(models.Model):
  """結果モデル"""

  class Meta:
    ordering = ['created_at']

  scan_time = models.DateTimeField()
  hostname = models.CharField(max_length=255)
  emocheck_version = models.CharField(max_length=255)
  is_infected = models.BooleanField(choices=[(True, 'yes'),(False, 'no')], default=False)
  created_at = models.DateTimeField(auto_now_add=True)


class EmotetProcess(models.Model):
  """Emotetプロセスモデル"""

  class Meta:
    ordering = ['created_at']

  result = models.ForeignKey(Result, on_delete=models.CASCADE)
  process_name = models.CharField(max_length=255)
  process_id = models.IntegerField()
  image_path = models.CharField(max_length=255)
  registry_key = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
