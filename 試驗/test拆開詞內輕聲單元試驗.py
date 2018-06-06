from unittest.case import TestCase, skip
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.基本物件.字 import 字
from 輕聲分析.分析 import 輕聲分析器


class 拆開詞內輕聲單元試驗(TestCase):

    def test無輕聲詞(self):
        參數 = 拆文分析器.對齊詞物件('照顧', 'tsiàu-kòo')
        分析器物件 = 輕聲分析器()
        self.assertEqual(
            len(分析器物件.拆開詞內輕聲(參數)), 1
        )

    def test干焦輕聲詞(self):
        參數 = 拆文分析器.對齊詞物件('喔', '--ooh')
        分析器物件 = 輕聲分析器()
        self.assertEqual(
            len(分析器物件.拆開詞內輕聲(參數)), 1
        )

    def test攏總兩个詞(self):
        參數 = 拆文分析器.對齊詞物件('靚喔', 'tsiâng--ooh')
        分析器物件 = 輕聲分析器()
        self.assertEqual(
            len(分析器物件.拆開詞內輕聲(參數)), 2
        )

    def test一个輕聲孤字詞(self):
        參數 = 拆文分析器.對齊詞物件('靚喔', 'tsiâng--ooh')
        分析器物件 = 輕聲分析器()
        結果喔 = 分析器物件.拆開詞內輕聲(參數)[1]
        self.assertEqual(
            結果喔,
            [字('喔', 'ooh')]
        )

    def test有保留輕聲標記(self):
        參數 = 拆文分析器.對齊詞物件('靚喔', 'tsiâng--ooh')
        分析器物件 = 輕聲分析器()
        結果喔 = 分析器物件.拆開詞內輕聲(參數)[1]
        self.assertEqual(
            結果喔[0].敢有輕聲標記(),
            True
        )

    def test兩个輕聲詞(self):
        參數 = 拆文分析器.對齊詞物件('靚一下一下', 'tsiâng--tsi̍t-ē--tsi̍t-ē')
        分析器物件 = 輕聲分析器()
        self.assertEqual(
            分析器物件.拆開詞內輕聲(參數)[-1],
            [字('一', 'tsi̍t'), 字('下', 'ē')]
        )

    def test攏總三个詞(self):
        參數 = 拆文分析器.對齊詞物件('靚一下一下', 'tsiâng--tsi̍t-ē--tsi̍t-ē')
        分析器物件 = 輕聲分析器()
        self.assertEqual(
            len(分析器物件.拆開詞內輕聲(參數)), 3
        )

    def test輕聲三字詞(self):
        參數 = 拆文分析器.對齊詞物件('靚淡薄仔', 'tsiâng--tām-po̍h-á')
        分析器物件 = 輕聲分析器()
        self.assertEqual(
            分析器物件.拆開詞內輕聲(參數)[-1],
            [字('淡', 'tām', 輕聲標記=True), 字('薄', 'po̍h'), 字('仔', 'á')]
        )
