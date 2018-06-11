from unittest.case import TestCase
from 輕聲分析.分析 import 輕聲分析器
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器


class 決定詞內的分連寫mock單元試驗(TestCase):
    def setUp(self):
        # 初始物件了後，佇逐个試驗內底改清單
        self.分析器物件 = 輕聲分析器()

    def tearDown(self):
        一詞 = 拆文分析器.對齊詞物件(self.漢字, self.臺羅)
        self.assertEqual(
            self.分析器物件.決定詞內的分連寫(一詞, self.輕聲位),
            self.按算結果
        )

    def test清單愛先對著較長的收詞__來去媠(self):
        self.分析器物件.清單 = {
            '分寫清單': ['來-去｜lâi-khì'],
            '連寫清單': ['來｜lâi'],
        }
        self.漢字 = '林來去靚'
        self.臺羅 = 'Lîm--lâi-khì-tsiâng'
        self.輕聲位 = [1]
        self.按算結果 = [True]

    def test清單對著較短的收詞__來靚(self):
        self.分析器物件.清單 = {
            '分寫清單': ['來-去｜lâi-khì'],
            '連寫清單': ['來｜lâi'],
        }
        self.漢字 = '林來靚'
        self.臺羅 = 'Lîm--lâi-tsiâng'
        self.輕聲位 = [1]
        self.按算結果 = [False]
