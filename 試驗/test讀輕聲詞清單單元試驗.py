from unittest.case import TestCase
from 輕聲分析.輕聲詞清單 import 讀輕聲詞清單


class 讀輕聲詞清單單元試驗(TestCase):
    def test讀著愛拆開的詞(self):
        拆開清單 = 讀輕聲詞清單()[0]
        self.assertIn('我｜guá', 拆開清單)
    
    def test讀著愛連寫的詞(self):
        連寫清單 = 讀輕聲詞清單()[1]
        self.assertIn('媽｜mah', 連寫清單)