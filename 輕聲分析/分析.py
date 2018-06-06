from 輕聲分析.輕聲詞清單 import 讀輕聲詞清單
from 臺灣言語工具.基本物件 import 詞

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
        for 詞物件 in 句物件.網出詞物件():
            # 無分開的愛分開
            新的詞陣列 = self.拆開詞內輕聲(詞物件)
        return

    def 拆開詞內輕聲(self, 詞物件):
        結果詞陣列 = []
        for 字物件 in 詞物件.篩出字物件():
            字分詞 = 字物件.看分詞()
            if (
                字物件.敢有輕聲標記() and
                字分詞 in self.清單['拆開清單']
            ):
                # 該輕聲詞是新的詞
                結果詞陣列.append([字物件])
            elif not 結果詞陣列:
                # 頭字
                結果詞陣列.append([字物件])
            else:
                # 後壁的一般非輕聲的字
                結果詞陣列[-1].append(字物件)
                
        return 結果詞陣列 