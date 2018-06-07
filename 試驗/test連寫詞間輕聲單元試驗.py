from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 輕聲分析.分析 import 輕聲分析器
from 臺灣言語工具.基本物件.字 import 字


class 連寫詞間輕聲單元試驗(TestCase):
    def test連一个詞A__B(self):
        參數 = [[字('媽', 'ma')], [字('媽', 'mah', 輕聲標記=True)]]
        分析器物件 = 輕聲分析器()
        self.assertEqual(
            分析器物件.連寫詞間輕聲(參數)[0],
            [字('媽', 'ma'), 字('媽', 'mah', 輕聲標記=True)]
        )

    def test連一个濟字詞A__BC(self):
        參數 = [[字('轉', 'tńg')], [字('來', 'lâi', 輕聲標記=True), ('去', 'khì')]]
        分析器物件 = 輕聲分析器()
        self.assertEqual(
            分析器物件.連寫詞間輕聲(參數)[0],
            [字('轉', 'tńg'), 字('來', 'lâi', 輕聲標記=True), ('去', 'khì')]
        )

    def test莫振動著後壁的一般詞A__BC_E(self):
        參數 = [
            [字('轉', 'tńg')],
            [字('來', 'lâi', 輕聲標記=True), ('去', 'khì')],
            [字('媠', 'suí')]
        ]
        分析器物件 = 輕聲分析器()
        self.assertEqual(
            len(分析器物件.連寫詞間輕聲(參數)), 2
        )

    def test攏一般詞A_BC(self):
        參數 = [
            [字('媠', 'suí')]
            [字('姑', 'koo'), ('娘', 'niû')],
        ]
        拆文分析器.對齊句物件('媠姑娘', 'suí koo-niû')
        分析器物件 = 輕聲分析器()
        self.assertEqual(
            len(分析器物件.連寫詞間輕聲(參數)), 2
        )

    def test干焦輕聲詞__A(self):
        參數 = [[字('喔', 'ooh', 輕聲標記=True)]]
        分析器物件 = 輕聲分析器()
        self.assertEqual(
            len(分析器物件.連寫詞間輕聲(參數)), 1
        )
