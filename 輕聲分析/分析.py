from 臺灣言語工具.基本物件.詞 import 詞
from 臺灣言語工具.基本物件.集 import 集
from 臺灣言語工具.基本物件.組 import 組
from 臺灣言語工具.基本物件.句 import 句
from 輕聲分析.輕聲詞清單 import 輕聲詞清單
from 臺灣言語工具.基本物件.公用變數 import 標點符號


class 輕聲分析器():

    def __init__(self):
        self.清單 = 輕聲詞清單.讀輕聲詞清單()

    def 輕聲分析(self, 句物件):
        #
        # 揣出輕聲詞，看伊是愛kap頭前抑是分開。
        # 無分開 我是媠--喔 => 我是媠 --喔
        # 無kap  王 --先生  => 王--先生
        #
        拆好詞陣列 = self.拆開輕聲(句物件)
        規句詞陣列 = self.連寫詞間輕聲(拆好詞陣列)
        # 轉換做句物件
        詞陣列 = []
        for 詞字陣列 in 規句詞陣列:
            詞陣列.append(詞(詞字陣列))
        新句物件 = 句([
            集([
                組(詞陣列)
            ])
        ])
        return 新句物件

    def 拆開輕聲(self, 句物件):
        規句的詞陣列 = []
        for 詞物件 in 句物件.網出詞物件():
            if 詞物件.看型() == '有的無的':
                新的詞陣列 = [詞物件.篩出字物件()]
            else:
                # 無分開的愛分開
                新的詞陣列 = self.拆開詞內輕聲(詞物件)
            規句的詞陣列 += 新的詞陣列
        return 規句的詞陣列

    def 拆開詞內輕聲(self, 詞物件):
        # 有的詞可能是一般詞+輕聲詞的詞組，愛共in拆做兩个詞。
        # A--B-C => A, --B-C
        詞組陣列 = []
        輕聲位置陣列 = self.提詞內輕聲位置(詞物件)
        分連寫陣列 = self.決定詞內的分連寫(詞物件, 輕聲位置陣列)
        # 共位kah分連寫先kap做伙
        位對應寫陣列 = {}
        for 索引, 輕聲位 in enumerate(輕聲位置陣列):
            位對應寫陣列[輕聲位] = 分連寫陣列[索引]
        # 拆詞
        詞內的字陣列 = 詞物件.篩出字物件()
        for 字索引, 字物件 in enumerate(詞內的字陣列):
            # 是愛拆開的輕聲字
            if 字物件.敢有輕聲標記() and 位對應寫陣列[字索引]:
                詞組陣列.append([字物件])
            # 一般字
            else:
                # kah頭前連寫
                if not 詞組陣列:
                    詞組陣列.append([字物件])
                else:
                    詞組陣列[-1].append(字物件)

        return 詞組陣列

    def 提詞內輕聲位置(self, 詞物件):
        輕聲位置陣列 = []
        詞內的字陣列 = 詞物件.篩出字物件()
        for 字索引, 字物件 in enumerate(詞內的字陣列):
            if 字物件.敢有輕聲標記():
                輕聲位置陣列.append(字索引)
        return 輕聲位置陣列

    def 決定詞內的分連寫(self, 詞物件, 輕聲位陣列):
        分連寫陣列 = []
        詞內的字陣列 = 詞物件.篩出字物件()
        # 無輕聲詞
        if not 輕聲位陣列:
            return 分連寫陣列

        # 第一个位 kah 後壁的位分開
        位頭 = 輕聲位陣列[0]
        tshun的輕聲位陣列 = 輕聲位陣列[1:]

        # 提出第一个詞的字
        try:
            # 用第二個輕聲詞的頭位做第一个輕聲詞的尾位
            位尾 = tshun的輕聲位陣列[0]
        except IndexError:
            # 做到上尾矣，只好用詞長度當做尾位
            位尾 = len(詞內的字陣列)
        # 判斷第一个詞的分連寫
        # 比對著上長的收詞為準
        是分寫詞 = False
        while 位尾 > 位頭:
            輕聲詞分詞 = 詞(詞內的字陣列[位頭: 位尾]).看分詞()
            if 輕聲詞分詞 in self.清單['分寫清單']:
                是分寫詞 = True
                break
            else:
                位尾 -= 1
        分連寫陣列.append(是分寫詞)

        # 後壁的輕聲詞攏一定分寫
        for _dummy in tshun的輕聲位陣列:
            分連寫陣列.append(True)
        return 分連寫陣列

    def 連寫詞間輕聲(self, 一句詞陣列):
        # 當詞在連寫清單，而且頭前的詞無輕聲詞，
        # 輕聲詞著愛kah頭前的詞連寫。
        # 佇拆開詞內輕聲之後，詞的可能型態：
        # 一般--連連, 一般--免免, 一般, --分分, --連連, --免免
        新的詞陣列 = []
        頭前有輕聲詞 = False
        頂一个詞是標點符號 = False

        for 該詞 in 一句詞陣列:
            一詞字陣列 = 該詞[:]
            頭字物件 = 一詞字陣列[0]
            # 輕聲詞
            # --分分, --連連, --免免
            if 頭字物件.敢有輕聲標記() and not 頭前有輕聲詞 and not 頂一个詞是標點符號:
                判斷書寫 = None
                # 判斷這詞敢有收佇連寫清單
                巡字索引 = len(一詞字陣列)
                while 巡字索引:
                    詞分詞 = 詞(一詞字陣列[:巡字索引]).看分詞()
                    if 詞分詞 in self.清單['連寫清單']:
                        判斷書寫 = '連寫'
                        break
                    elif 詞分詞 in self.清單['分寫清單']:
                        判斷書寫 = '分寫'
                        break
                    else:
                        巡字索引 -= 1
                # 是連寫詞
                if 判斷書寫 == '連寫':
                    try:
                        新的詞陣列[-1] += 一詞字陣列
                    except IndexError:
                        新的詞陣列.append(一詞字陣列)
                # 是分寫詞
                elif 判斷書寫 == '分寫':
                    新的詞陣列.append(一詞字陣列)
                # 是免處理詞，照原本分寫的就好
                else:
                    新的詞陣列.append(一詞字陣列)
                頭前有輕聲詞 = True
            # 一般詞、一般詞但是已經有接輕聲詞、連續第二个的輕聲詞、標點符號
            # 一般--連連, 一般--免免, 一般--連連 --連連,，｜,
            else:
                新的詞陣列.append(一詞字陣列)
                詞內有輕聲 = False
                for 字物件 in 一詞字陣列:
                    if 字物件.敢有輕聲標記():
                        詞內有輕聲 = True
                        break
                頭前有輕聲詞 = 詞內有輕聲

            # 該詞敢是標點符號
            if 頭字物件.看型() in 標點符號 or 頭字物件.看音() in 標點符號:
                頂一个詞是標點符號 = True
            else:
                頂一个詞是標點符號 = False
        return 新的詞陣列
