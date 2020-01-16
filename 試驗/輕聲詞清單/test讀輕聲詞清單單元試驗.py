from unittest.case import TestCase
from 輕聲分析.輕聲詞清單 import 輕聲詞清單


class 讀輕聲詞清單單元試驗(TestCase):
    def test讀著愛分寫的詞(self):
        分寫清單 = 輕聲詞清單.讀輕聲詞清單()['分寫清單']
        self.assertIn('--我｜--guá', 分寫清單)

    def test讀著愛分寫的濟字詞(self):
        分寫清單 = 輕聲詞清單.讀輕聲詞清單()['分寫清單']
        self.assertIn('--先-生｜--sian-sinn', 分寫清單)

    def test讀著愛連寫的詞(self):
        連寫清單 = 輕聲詞清單.讀輕聲詞清單()['連寫清單']
        self.assertIn('--媽｜--mah', 連寫清單)
