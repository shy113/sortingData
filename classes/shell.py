# *-* encoding:utf8 *_*
# Author       : GZH
# Date         : 2022年10月03日
# Description  : 希尔排序

class Shell:

    def sort(self, arr):
        # 1.根据数组a的长度，确定增量h
        h: int = 1
        while h < int(len(arr)) / int(2):
            h = 2 * h + 1
        # 2.希尔排序
        while h >= 1:
            # 2.1.找到待插入的元素
            for i in range(h, len(arr), 1):
                for j in range(i, h - 1, -h):
                    if self.greater(arr[j - h].featureId, arr[j].featureId):
                        self.exch(arr, j - h, j)
                    else:
                        # 待插入元素已经找到了合适的位置，结束循环 无需再向左比较
                        break
            h = int(h / 2)

    # 比较元素大小
    def greater(self, i, j):
        if i > j:
            return True
        return False

    # 交换元素位置
    def exch(self, arr, i, j):
        arriold, arrjold = arr[i], arr[j]
        arr[i], arr[j] = arrjold, arriold
