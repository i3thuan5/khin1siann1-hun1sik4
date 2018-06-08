from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 輕聲分析.分析 import 輕聲分析器
from unittest.mock import patch


class 決定詞內的分連寫單元試驗(TestCase):
    def tearDown(self):
        一詞 = 拆文分析器.對齊詞物件(self.漢字, self.臺羅)
        分析器物件 = 輕聲分析器()
        self.assertEqual(
            分析器物件.決定詞內的分連寫(一詞, self.輕聲位),
            self.按算結果
        )
    
    # 判斷清單內底有收的詞
    
    def test分寫的輕聲詞(self):
        self.漢字 = '林啦'
        self.臺羅 = 'Lîm--lah'
        self.輕聲位 = [1, ]
        self.按算結果 = [True]

    def test連寫的輕聲詞(self):
        self.漢字 = '林仔'
        self.臺羅 = 'Lîm--á'
        self.輕聲位 = [1, ]
        self.按算結果 = [False]

    def test第二个以後的輕聲詞一定拆開(self):
        self.漢字 = '林啦仔啦'
        self.臺羅 = 'Lîm--lah--á--lah'
        self.輕聲位 = [1, 2, 3]
        self.按算結果 = [True, True, True]

    def test干焦兩个輕聲詞(self):
        self.漢字 = '先生啦'
        self.臺羅 = '--sian-sinn--lah'
        self.輕聲位 = [0, 2, ]
        self.按算結果 = [True, True, ]

    def test無輕聲詞(self):
        self.漢字 = '林'
        self.臺羅 = 'Lîm'
        self.輕聲位 = []
        self.按算結果 = []

    def test清單衍生詞__一下(self):
        self.漢字 = '靚一下一下'
        self.臺羅 = 'tsiâng--tsi̍t-ē--tsi̍t-ē'
        self.輕聲位 = [1, 3]
        self.按算結果 = [True, True]

    @patch('輕聲分析.輕聲詞清單.輕聲詞清單.讀輕聲詞清單')
    def test清單愛先對著較長的收詞__來去媠(self, 清單mock):
        清單mock.return_value = [
            ['來-去｜lâi-khì'],  # 拆開清單
            ['來｜lâi']  # 連寫清單
        ]
        self.漢字 = '林來去靚'
        self.臺羅 = 'Lîm--lâi-khì-tsiâng'
        self.輕聲位 = [1]
        self.按算結果 = [True]

    @patch('輕聲分析.輕聲詞清單.輕聲詞清單.讀輕聲詞清單')
    def test清單對著較短的收詞__來靚(self, 清單mock):
        清單mock.return_value = [
            ['來-去｜lâi-khì'],  # 拆開清單
            ['來｜lâi']  # 連寫清單
        ]
        self.漢字 = '林來靚'
        self.臺羅 = 'Lîm--lâi-tsiâng'
        self.輕聲位 = [1]
        self.按算結果 = [False]
    
    # 判斷清單內底無收的詞
    
    def test清單無收就維持連寫林__靚(self):
        self.漢字 = '林靚'
        self.臺羅 = 'Lîm--tsiâng'
        self.輕聲位 = [0, ]
        self.按算結果 = [False]

    def test清單無收這个輕聲詞__靚(self):
        self.漢字 = '靚'
        self.臺羅 = '--tsiâng'
        self.輕聲位 = [0, ]
        self.按算結果 = [False]

    def test清單無收遮的輕聲詞__靚(self):
        self.漢字 = '靚靚'
        self.臺羅 = '--tsiâng--tsiâng'
        self.輕聲位 = [0, 1]
        self.按算結果 = [False, True]