from django.test import TestCase
from .serializers import ResultSerializer

class TestResultSerializer(TestCase):
  """ResultSerializerのテスト"""

  def test_input_valid(self):
    """入力データのバリデーション(OK)"""

    input_data = {
      'scan_time': '2023-01-09 11:02:07',
      'hostname': 'ASDFGHJK',
      'emocheck_version': '0.1.0',
      'is_infected': 'yes'
    }

    serializer = ResultSerializer(data=input_data)

    self.assertEqual(serializer.is_valid(), True)
