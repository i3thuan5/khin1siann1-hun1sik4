from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 輕聲分析.分析 import 輕聲分析器


class 輕聲分析器整合試驗(TestCase):

    def tearDown(self):
        參數 = 拆文分析器.對齊句物件(self.漢字, self.原臺羅)
        按算結果 = 拆文分析器.對齊句物件(self.漢字, self.按算臺羅)
        # 執行測試
        分析器物件 = 輕聲分析器()
        self.assertEqual(
            分析器物件.輕聲分析(參數), 按算結果
        )

    def test頭前kap(self):
        # A --B --C =>
        # A--B, --C
        self.漢字 = '林仔啦'
        self.原臺羅 = 'Lîm --á --lah'
        self.按算臺羅 = 'Lîm--á --lah'

    def test頭前kap後壁拆開(self):
        # A --B--C =>
        # A--B, --C
        self.漢字 = '林仔啦'
        self.原臺羅 = 'Lîm --á--lah'
        self.按算臺羅 = 'Lîm--á --lah'

    def test後壁斷開(self):
        # A --B--C =>
        # A, --B, --C
        self.漢字 = '林先生啦'
        self.原臺羅 = 'Lîm --sian-sinn--lah'
        self.按算臺羅 = 'Lîm --sian-sinn --lah'

    def test斷開兩个(self):
        # A--B-C--D E =>
        # A, B-C, D, E
        self.漢字 = '照顧一下啦你'
        self.原臺羅 = 'tsiàu-kòo--tsi̍t-ē--lah lí'
        self.按算臺羅 = 'tsiàu-kòo --tsi̍t-ē --lah lí'

    def test無收的詞維持分寫(self):
        self.漢字 = '照顧媠媠啦你'
        self.原臺羅 = 'tsiàu-kòo --suí-suí--lah lí'
        self.按算臺羅 = 'tsiàu-kòo --suí-suí --lah lí'

    def test無收的詞維持連寫(self):
        self.漢字 = '照顧媠媠啦你'
        self.原臺羅 = 'tsiàu-kòo--suí-suí--lah lí'
        self.按算臺羅 = 'tsiàu-kòo--suí-suí --lah lí'
    
    def test動補的詞維持分寫(self):
        self.漢字 = '照顧起來'
        self.原臺羅 = 'tsiàu-kòo --khí-lâi'
        self.按算臺羅 = 'tsiàu-kòo --khí-lâi'

    def test動補的詞維持連寫(self):
        self.漢字 = '照顧起來'
        self.原臺羅 = 'tsiàu-kòo--khí-lâi'
        self.按算臺羅 = 'tsiàu-kòo--khí-lâi'
        
    def test標點符號(self):
        self.漢字 = '林仔啦！'
        self.原臺羅 = 'Lîm--á --lah!'
        self.按算臺羅 = 'Lîm--á --lah !'
