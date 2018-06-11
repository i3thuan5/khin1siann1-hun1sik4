from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 輕聲分析.分析 import 輕聲分析器


class 提詞內輕聲位置單元試驗(TestCase):
    def tearDown(self):
        一詞 = 拆文分析器.對齊詞物件(self.漢字, self.臺羅)
        分析器物件 = 輕聲分析器()
        self.assertEqual(
            分析器物件.提詞內輕聲位置(一詞),
            self.按算結果
        )

    def test有兩个輕聲詞(self):
        self.漢字 = '林先生啦'
        self.臺羅 = 'Lîm--sian-sinn--lah'
        self.按算結果 = [1, 3]

    def test干焦兩个輕聲詞(self):
        self.漢字 = '先生啦'
        self.臺羅 = '--sian-sinn--lah'
        self.按算結果 = [0, 2, ]
