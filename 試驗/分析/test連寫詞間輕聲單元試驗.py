from unittest.case import TestCase
from 輕聲分析.分析 import 輕聲分析器
from 臺灣言語工具.基本物件.字 import 字


class 連寫詞間輕聲單元試驗(TestCase):

    #
    # A 一般詞 姑娘
    # B 清單的分寫詞 --喔
    # C 清單的連寫詞 --仔
    #
    def setUp(self):
        self.分析器物件 = 輕聲分析器()

    def tearDown(self):
        self.assertEqual(
            self.分析器物件.連寫詞間輕聲(self.參數),
            self.按算結果
        )

    def test連孤字詞A__B(self):
        self.參數 = [
            [字('媽', 'ma')],
            [字('媽', 'mah', 輕聲標記=True)]
        ]
        self.按算結果 = [[字('媽', 'ma'), 字('媽', 'mah', 輕聲標記=True)]]

    def test連濟字詞A__BC(self):
        # 因為濟字詞大部份是動詞補語，但是補語目前無愛處理，
        # 所以用mock清單的方式試驗
        self.分析器物件.清單 = {
            '分寫清單': [],
            '連寫清單': ['--來-去｜--lâi-khì'],
        }
        self.參數 = [
            [字('轉', 'tńg')],
            [字('來', 'lâi', 輕聲標記=True), 字('去', 'khì')]
        ]
        self.按算結果 = [[字('轉', 'tńg'), 字('來', 'lâi', 輕聲標記=True), 字('去', 'khì')]]

    def test莫振動著後壁A__BC_E(self):
        # 因為濟字詞大部份是動詞補語，但是補語目前無愛處理，
        # 所以用mock清單的方式試驗
        self.分析器物件.清單 = {
            '分寫清單': [],
            '連寫清單': ['--來-去｜--lâi-khì'],
        }
        self.參數 = [
            [字('轉', 'tńg')],
            [字('來', 'lâi', 輕聲標記=True), 字('去', 'khì')],
            [字('媠', 'suí')]
        ]
        self.按算結果 = [
            [字('轉', 'tńg'), 字('來', 'lâi', 輕聲標記=True), 字('去', 'khì')],
            [字('媠', 'suí')]
        ]

    def test攏一般詞A_BC(self):
        self.參數 = [
            [字('媠', 'suí')],
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

    def test頭前已經連寫過矣A__C__C(self):
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

    def test句頭輕聲詞(self):
        self.參數 = [
            [字('仔', 'á', 輕聲標記=True)],
        ]
        self.按算結果 = self.參數

    def test句頭輕聲詞莫影響後壁詞(self):
        self.參數 = [
            [字('仔', 'á', 輕聲標記=True)],
            [字('姑', 'koo'), 字('娘', 'niû')],
        ]
        self.按算結果 = self.參數

    def test標點符號不接輕聲詞(self):
        self.參數 = [
            [字('，', ',')],
            [字('仔', 'á', 輕聲標記=True)],
        ]
        self.按算結果 = self.參數

    def test標點符號不接一般詞(self):
        self.參數 = [
            [字('，', ',')],
            [字('姑', 'koo'), 字('娘', 'niû')],
            [字('仔', 'á', 輕聲標記=True)],
        ]
        self.按算結果 = [
            [字('，', ',')],
            [字('姑', 'koo'), 字('娘', 'niû'), 字('仔', 'á', 輕聲標記=True)],
        ]

    def test詞不接標點符號(self):
        self.參數 = [
            [字('姑', 'koo'), 字('娘', 'niû')],
            [字('仔', 'á', 輕聲標記=True)],
            [字('，', ',')],
        ]
        self.按算結果 = [
            [字('姑', 'koo'), 字('娘', 'niû'), 字('仔', 'á', 輕聲標記=True)],
            [字('，', ',')],
        ]
