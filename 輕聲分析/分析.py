from 輕聲分析.輕聲詞清單 import 讀輕聲詞清單
from 臺灣言語工具.基本物件.詞 import 詞


class 輕聲分析器():

    def __init__(self):
        self.清單 = 讀輕聲詞清單()

    def 輕聲分析(self, 句物件):
        #
        # 揣出輕聲詞，看伊是愛kap頭前抑是分開。
        # 無分開 我是媠--喔 => 我是媠 --喔
        # 無kap  王 --先生  => 王--先生
        #
        拆好的句物件 = self.拆開輕聲(句物件)
        return 拆好的句物件

    def 拆開輕聲(self, 句物件):
        規句的詞陣列 = []
        for 詞物件 in 句物件.網出詞物件():
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
        for 輕聲位置陣列 
        
#         詞內的字陣列 = 詞物件.篩出字物件()
#         for 字索引, 字物件 in enumerate(詞內的字陣列):
#             # 輕聲詞頭字
#             if 字物件.敢有輕聲標記():
#                 輕聲詞分詞 = 詞(詞內的字陣列[字索引:]).看分詞()
#                 print(詞內的字陣列[字索引:])
#                 if 輕聲詞分詞 in self.清單['拆開清單']:
#                     # 該輕聲詞是後一个詞
#                     詞組陣列.append([字物件])
#             # 詞組頭字
#             elif not 詞組陣列:
#                 詞組陣列.append([字物件])
#             # 後壁的一般非輕聲的字
#             else:
#                 詞組陣列[-1].append(字物件)
#         return 詞組陣列

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
        
        # 第一個詞 kah 後壁的詞分開
        位頭 = 輕聲位陣列.pop(0)
        
        # 第一個輕聲詞愛判斷分連寫
        try:
            # 用第二個輕聲詞的頭位做第一个輕聲詞的尾位
            位尾 = 輕聲位陣列[0]
        except:
            位尾 = len(詞內的字陣列)
        if 位頭 == 位尾:
            # 孤字詞
            輕聲詞分詞 = 詞(詞內的字陣列[位頭]).看分詞()
        else:
            # 濟字詞
            輕聲詞分詞 = 詞(詞內的字陣列[位頭: 位尾]).看分詞()
        是分寫詞 = False
        if 輕聲詞分詞 in self.清單['拆開清單']:
            是分寫詞 = True
        分連寫陣列.append(是分寫詞)

        # 後壁的輕聲詞攏一定分寫
        for dummy in 輕聲位陣列:
            分連寫陣列.append(True)
        return 分連寫陣列

    def 連寫詞間輕聲(self, 一句的詞陣列):
        # 有的輕聲詞著愛kah頭前的詞連寫
        新的詞陣列 = []
        for 一詞的字陣列 in 一句的詞陣列:
            頭字物件 = 一詞的字陣列[0]
            print('頭字物件=', 頭字物件)
            # 愛連寫的輕聲詞頭字
            if 頭字物件.敢有輕聲標記():
                詞分詞 = 詞(一詞的字陣列).看分詞()
                print('詞分詞=', 詞分詞, 頭字物件.敢有輕聲標記())
                if 詞分詞 in self.清單['連寫清單']:
                    print('if')
                    # [[頭詞]] => [[頭詞, 輕聲詞]]
                    新的詞陣列[-1] += 一詞的字陣列
            # 頭字
            elif not 新的詞陣列:
                # [] => [[頭詞]]
                新的詞陣列.append(一詞的字陣列)
            # 一般非輕聲的詞
            else:
                # [[詞]] => [[詞], [新詞]]
                新的詞陣列.append(一詞的字陣列)
        return 新的詞陣列
