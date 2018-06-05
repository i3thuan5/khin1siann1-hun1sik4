from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 輕聲分析.分析 import 輕聲分析


class 輕聲分析整合試驗(TestCase):
    def test愛斷開的輕聲詞(self):
        參數 = 拆文分析器.對齊句物件('靚喔', 'tsiâng--oh')
        按算結果 = 拆文分析器.對齊句物件('靚喔', 'tsiâng --oh')
        self.assertEqual(
            輕聲分析(參數), 按算結果
        )