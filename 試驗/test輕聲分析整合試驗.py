from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 輕聲分析.分析 import 輕聲分析


class 輕聲分析整合試驗(TestCase):
    def test一个kap頭前(self):
        # A --B --C =>
        # A--B, --C
        漢字 = '林家啦'
        原臺羅 = 'Lîm --ka --lah'
        按算臺羅 = 'Lîm--ka --lah'
        參數 = 拆文分析器.對齊句物件(漢字, 原臺羅)
        按算結果 = 拆文分析器.對齊句物件(漢字, 按算臺羅)
        self.assertEqual(
            輕聲分析(參數), 按算結果
        )

    def test斷開一个(self):
        # A --B--C =>
        # A, --B, --C
        漢字 = '林先生啦'
        原臺羅 = 'Lîm --sian-sinn--lah'
        按算臺羅 = 'Lîm --sian-sinn --lah'
        參數 = 拆文分析器.對齊句物件(漢字, 原臺羅)
        按算結果 = 拆文分析器.對齊句物件(漢字, 按算臺羅)
        self.assertEqual(
            輕聲分析(參數), 按算結果
        )

    def test斷開兩个(self):
        # A--B-C--D E =>
        # A, B-C, D, E
        漢字 = '照顧一下啦你'
        原臺羅 = 'tsiàu-kòo--tsi̍t-ē--lah lí'
        按算臺羅 = 'tsiàu-kòo --tsi̍t-ē --lah lí'
        參數 = 拆文分析器.對齊句物件(漢字, 原臺羅)
        按算結果 = 拆文分析器.對齊句物件(漢字, 按算臺羅)
        self.assertEqual(
            輕聲分析(參數), 按算結果
        )
