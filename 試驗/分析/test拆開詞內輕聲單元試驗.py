from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.基本物件.字 import 字
from 輕聲分析.分析 import 輕聲分析器


class 拆開詞內輕聲單元試驗(TestCase):

    def test無輕聲詞(self):
        參數 = 拆文分析器.對齊詞物件('照顧', 'tsiàu-kòo')
        分析器物件 = 輕聲分析器()
        self.assertEqual(
            分析器物件.拆開詞內輕聲(參數),
            [[字('照', 'tsiàu'), 字('顧', 'kòo')]]
        )

    def test干焦輕聲詞(self):
        參數 = 拆文分析器.對齊詞物件('喔', '--ooh')
        分析器物件 = 輕聲分析器()
        self.assertEqual(
            分析器物件.拆開詞內輕聲(參數),
            [[字('喔', 'ooh', 輕聲標記=True)]]
        )

    def test一个輕聲孤字詞(self):
        參數 = 拆文分析器.對齊詞物件('靚喔', 'tsiâng--ooh')
        分析器物件 = 輕聲分析器()
        self.assertEqual(
            分析器物件.拆開詞內輕聲(參數),
            [[字('靚', 'tsiâng')], [字('喔', 'ooh', 輕聲標記=True)]]
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
            分析器物件.拆開詞內輕聲(參數),
            [
                [字('靚', 'tsiâng'), ],
                [字('一', 'tsi̍t', 輕聲標記=True), 字('下', 'ē')],
                [字('一', 'tsi̍t', 輕聲標記=True), 字('下', 'ē')],
            ]
        )

    def test輕聲三字詞(self):
        參數 = 拆文分析器.對齊詞物件('靚淡薄仔', 'tsiâng--tām-po̍h-á')
        分析器物件 = 輕聲分析器()
        self.assertEqual(
            分析器物件.拆開詞內輕聲(參數),
            [
                [字('靚', 'tsiâng'), ],
                [字('淡', 'tām', 輕聲標記=True), 字('薄', 'po̍h'), 字('仔', 'á')]
            ]
        )

    def test莫拆著連寫的輕聲詞(self):
        參數 = 拆文分析器.對齊詞物件('林仔啦', 'Lîm--á--lah')
        分析器物件 = 輕聲分析器()
        self.assertEqual(
            分析器物件.拆開詞內輕聲(參數),
            [
                [字('林', 'Lîm'), 字('仔', 'á', 輕聲標記=True), ],
                [字('啦', 'lah', 輕聲標記=True)]
            ]
        )

    def test無收的詞維持原本連寫(self):
        參數 = 拆文分析器.對齊詞物件('林靚', 'Lîm--tsiâng')
        分析器物件 = 輕聲分析器()
        self.assertEqual(
            分析器物件.拆開詞內輕聲(參數),
            [[字('林', 'Lîm'), 字('靚', 'tsiâng', 輕聲標記=True), ]]
        )
