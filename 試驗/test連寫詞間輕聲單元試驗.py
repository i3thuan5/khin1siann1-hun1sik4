from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 輕聲分析.分析 import 輕聲分析器
from 臺灣言語工具.基本物件.字 import 字


class 連寫詞間輕聲單元試驗(TestCase):
    def test連一个詞A__B(self):
        參數 = 拆文分析器.對齊句物件('媽媽', 'ma --mah').
        分析器物件 = 輕聲分析器()
        self.assertEqual(
            分析器物件.連寫詞間輕聲(參數)[0],
            [字('媽', 'ma'), 字('媽', 'mah')]
        )

    def test連一个濟字詞A__B_C(self):
        參數 = 拆文分析器.對齊句物件('轉來去', 'tńg --lâi-khì')
        分析器物件 = 輕聲分析器()
        self.assertEqual(
            len(分析器物件.連寫詞間輕聲(參數)), 1
        )

    def test莫振動著後壁的一般詞(self):
        參數 = 拆文分析器.對齊句物件('轉來去媽', 'tńg --lâi-khì ma')
        分析器物件 = 輕聲分析器()
        self.assertEqual(
            len(分析器物件.連寫詞間輕聲(參數)), 3
        )

    def test攏一般詞(self):
        參數 = 拆文分析器.對齊句物件('媠媠姑娘', 'suí suí koo-niû')
        分析器物件 = 輕聲分析器()
        self.assertEqual(
            len(分析器物件.連寫詞間輕聲(參數)), 3
        )
    
    def test干焦輕聲詞(self):
        參數 = 拆文分析器.對齊詞物件('喔', '--ooh')
        分析器物件 = 輕聲分析器()
        self.assertEqual(
            len(分析器物件.連寫詞間輕聲(參數)), 1
        )