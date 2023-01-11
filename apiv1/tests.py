from django.test import TestCase
from .serializers import ResultModelSerializer
from emocheck.models import Result


VALID_YES = {
  'scan_time': '2023-01-09 11:02:07',
  'hostname': 'ASDFGHJK',
  'emocheck_version': '0.1.0',
  'is_infected': 'yes',
  'emotet_processes': [{
    'process_name': 'mtask.exe',
    'process_id': '716',
    'image_path': 'C:\\Users\\[usename]\\AppData\\Local\\mstask.exe',
    'registry_key': 'HOGEHOGE'
  }]
}

INVALID_YES = {
  'scan_time': '2023-01-09 11:02:07',
  'hostname': 'ASDFGHJK',
  'emocheck_version': '0.1.0',
  'is_infected': 'hoge',
  'emotet_processes': [{
    'process_name': 'mtask.exe',
    'process_id': '716',
    'image_path': 'C:\\Users\\[usename]\\AppData\\Local\\mstask.exe'
  }]
}

VALID_NO = {
  'scan_time': '2023-01-09 11:02:07',
  'hostname': 'ASDFGHJK',
  'emocheck_version': '0.1.0',
  'is_infected': 'no'
}

INVALID_NO = {
  'scan_time': '2023-01-09 11:02:07',
  'hostname': 'ASDFGHJK',
  'emocheck_version': '0.1.0',
  'is_infected': 'hoge'
}


class TestResultModelSerializer(TestCase):
  """ResultSerializerのテスト"""

  def test_input_valid_yes(self):
    """入力データのバリデーション(OK)"""

    input_data = VALID_YES

    serializer = ResultModelSerializer(data=input_data)

    actual = serializer.is_valid()
    if not actual:
      print(serializer.errors)
    self.assertEqual(actual, True)

  def test_input_output_equal_yes(self):
    """入力データを出力データの比較"""

    input_data = VALID_YES

    serializer = ResultModelSerializer(data=input_data)

    actual = serializer.is_valid()
    if not actual:
      print(serializer.errors)
    self.assertEqual(actual, True)

    instance = serializer.save()

    serializer2 = ResultModelSerializer(instance=instance)

    self.assertDictEqual(serializer2.data, input_data)

  def test_save_valid_yes(self):
    """入力データをセーブ"""

    input_data = VALID_YES

    serializer = ResultModelSerializer(data=input_data)

    actual = serializer.is_valid()
    if not actual:
      print(serializer.errors)
    self.assertEqual(actual, True)

    serializer.save()
