from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 輕聲分析.分析 import 輕聲分析器
from 臺灣言語工具.基本物件.字 import 字


class 連寫詞間輕聲單元試驗(TestCase):
    #
    # A 一般詞 姑娘
    # B 清單的分寫詞 --喔
    # C 清單的連寫詞 --仔 
    #
    def tearDown(self):
        分析器物件 = 輕聲分析器()
        self.assertEqual(
            分析器物件.連寫詞間輕聲(self.參數),
            self.按算結果
        )
        
    def test連孤字詞A__B(self):
        self.參數 = [
            [字('媽', 'ma')], 
            [字('媽', 'mah', 輕聲標記=True)]
        ]
        self.按算結果 = [[字('媽', 'ma'), 字('媽', 'mah', 輕聲標記=True)]]

    def test連濟字詞A__BC(self):
        self.參數 = [
            [字('轉', 'tńg')], 
            [字('來', 'lâi', 輕聲標記=True), 字('去', 'khì')]
        ]
        self.按算結果 = [[字('轉', 'tńg'), 字('來', 'lâi', 輕聲標記=True), 字('去', 'khì')]]

    def test莫振動著後壁A__BC_E(self):
        self.參數 = [
            [字('轉', 'tńg')],
            [字('來', 'lâi', 輕聲標記=True), 字('去', 'khì')],
            [字('媠', 'suí')]
        ]
        self.按算結果 = self.參數

    def test攏一般詞A_BC(self):
        self.參數 = [
            [字('媠', 'suí')]
            [字('姑', 'koo'), 字('娘', 'niû')],
        ]
        self.按算結果 = self.參數

    def test干焦輕聲詞__B(self):
        self.參數 = [[字('喔', 'ooh', 輕聲標記=True)]]
        self.按算結果 = self.參數
        
    
    def test莫kah輕聲詞連做伙__B__C(self):
        self.參數 = [
            [字('喔', 'ooh', 輕聲標記=True)],
            [字('仔', 'á', 輕聲標記=True)],
        ]
        self.按算結果 = self.參數
    
    def test頭前已經有輕聲詞就莫連做伙A__C__C(self):
        self.參數 = [
            [字('姑', 'koo'), 字('娘', 'niû'), 字('仔', 'á', 輕聲標記=True)],
            [字('仔', 'á', 輕聲標記=True)],
        ]
        self.按算結果 = self.參數
    
    def test無收的詞維持原本分寫(self):
        # 姑娘--a --tsiang => 不變
        self.參數 = [
            [字('姑', 'koo'), 字('娘', 'niû'), 字('仔', 'á', 輕聲標記=True)],
            [字('靚', 'tsiâng', 輕聲標記=True)],
        ]
        self.按算結果 = self.參數