from django.test import TestCase
from .serializers import ResultModelSerializer
from emocheck.models import Result


class TestResultModelSerializer(TestCase):
  """ResultSerializerのテスト"""

  def test_input_valid(self):
    """入力データのバリデーション(OK)"""

    input_data = {
      'scan_time': '2023-01-09 11:02:07',
      'hostname': 'ASDFGHJK',
      'emocheck_version': '0.1.0',
      'is_infected': 'yes'
    }

    serializer = ResultModelSerializer(data=input_data)

    self.assertEqual(serializer.is_valid(), True)

  def test_input_output_equal(self):
    """入力データを出力データの比較"""

    input_data = {
      'scan_time': '2023-01-09 11:02:07',
      'hostname': 'ASDFGHJK',
      'emocheck_version': '0.1.0',
      'is_infected': 'yes'
    }

    serializer = ResultModelSerializer(data=input_data)

    self.assertEqual(serializer.is_valid(), True)

    instance = serializer.save()

    serializer2 = ResultModelSerializer(instance=instance)

    self.assertDictEqual(serializer2.data, input_data)

  def test_save_valid(self):
    """入力データをセーブ"""

    input_data = {
      'scan_time': '2023-01-09 11:02:07',
      'hostname': 'ASDFGHJK',
      'emocheck_version': '0.1.0',
      'is_infected': 'yes'
    }

    serializer = ResultModelSerializer(data=input_data)

    actual = serializer.is_valid()

    self.assertEqual(actual, True)

    serializer.save()
