from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.基本物件.詞 import 詞
from 輕聲分析.分析 import 拆開詞內輕聲


class 拆開詞內輕聲單元試驗(TestCase):

    def test無輕聲詞(self):
        參數 = 拆文分析器.對齊詞物件('照顧', 'tsiàu-kòo')
        self.assertEqual(
            len(拆開詞內輕聲(參數)), 1
        )

    def test攏總兩个詞(self):
        參數 = 拆文分析器.對齊詞物件('靚喔', 'tsiâng--ooh')
        self.assertEqual(
            len(拆開詞內輕聲(參數)), 2
        )

    def test一个輕聲孤字詞(self):
        參數 = 拆文分析器.對齊詞物件('靚喔', 'tsiâng--ooh')
        self.assertEqual(
            拆開詞內輕聲(參數)[1],
            詞('喔', '--ooh')
        )

    def test一个輕聲雙字詞(self):
        參數 = 拆文分析器.對齊詞物件('照顧一下', 'tsiàu-kòo--tsi̍t-ē')
        self.assertEqual(
            拆開詞內輕聲(參數)[1],
            詞('一下', '--tsi̍t-ē')
        )

    def test兩个輕聲詞(self):
        參數 = 拆文分析器.對齊詞物件('靚一下一下', 'tsiâng--tsi̍t-ē--tsi̍t-ē')
        self.assertEqual(
            拆開詞內輕聲(參數)[1],
            詞('一下', '--tsi̍t-ē')
        )

    def test攏總三个詞(self):
        參數 = 拆文分析器.對齊詞物件('靚一下一下', 'tsiâng--tsi̍t-ē--tsi̍t-ē')
        self.assertEqual(
            len(拆開詞內輕聲(參數)), 3
        )
