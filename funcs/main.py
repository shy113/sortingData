# *-* encoding:utf8 *_*
# Author       : GZH
# Date         : 2022年10月28日
# Description  : python处理excel
import os

import xlrd
import xlwt


# xlrd = 1.2.0


# 初始工作
def initData(filename, sheetname):
    '''
    获取指定文件中指定表的数据
    :param filename: excel文件名
    :param sheetname: 表名
    :return:
    '''
    xlsx = xlrd.open_workbook(filename)
    table_data = xlsx.sheet_by_name(sheetname)
    return xlsx, table_data


# 根据列名(字段名称)获取相应序号
def getColumnIndex(table_data, columnName):
    columnIndex = None
    for i in range(table_data.ncols):
        # table.ncols 有效列数
        if (table_data.cell_value(0, i) == columnName):
            columnIndex = i
            break
    return columnIndex


# 根据列索引获得去重属性列表
def getNoReppetList(table, columnIndex):
    list = []
    # 有效行数 有效列数
    effectiveRow, effectiveCol = table.nrows, table.ncols
    for i in range(effectiveRow):
        if not i == 0:  # 排除标题行
            val = table.cell_value(i, columnIndex)
            if val not in list:
                list.append(val)
    return list


# 构造所有数据列表
def getAllDatalist(table_data):
    '''
    构造表中所有数据 列表
    :return: 构造好的列表
    '''
    list = []
    effectiveRow, effectiveCol = table_data.nrows, table_data.ncols
    for ri in range(effectiveRow):
        rowDatalist = []
        for ci in range(effectiveCol):
            # 产品属性
            rowDatalist.append(table_data.cell_value(ri, ci))
        product_attribute = {
            'code': None,  # 代码
            'name': None,  # 名称
            'material_full_name': None,  # 物料全名
            'specifications': None,  # 规格型号
            'auxiliary_attribute_category_FName': None,  # 辅助属性类别_FName
            'auxiliary_attribute_category_FNumber': None,  # 辅助属性类别_FNumber
            'material_properties_FName': None,  # 物料属性_FName
            'default_repository_FName': None,  # 默认仓库_FName
            'default_repository_FNumber': None,  # 默认仓库_FNumber
            'Source_FName': None  # 来源_FName
        }

        i = 0
        for k, v in product_attribute.items():
            product_attribute[k] = rowDatalist[i]
            i += 1
        list.append(product_attribute)
    return list


# 整理好的数据重新写入新的表格
def write_excel_xls(list, sheetname, filename):
    '''
    将列表数据写入excel表格
    :param list: 存放数据的列表
    :param sheetname: 表名
    :param filename: 文件名
    :return:
    '''
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet(sheetname)
    r = 0
    for newitem in list:
        c = 0
        for k, v in newitem.items():
            worksheet.write(r, c, v)
            c += 1
        r += 1
    workbook.save(filename)


# 构造二合一列表(两个属性 A x B 个元素)
def get_unionlist(alist, blist):
    '''
    a x b 模式
    :param alist: 要合成的a列表
    :param blist: 要合成的b列表
    :return: 合成ab列表数据后的列表
    '''
    newlist = []
    for aitem in alist:
        for ditem in blist:
            classify_attribute = {
                'auxiliary_attribute_category_FName': aitem,  # 辅助属性类别_FName
                'default_repository_FName': ditem  # 默认仓库_FName
            }
            newlist.append(classify_attribute)
    return newlist


# 构造新的数据列表
def getnewData_list(newlist, oldlist, union_list):
    '''
    构造新的数据列表
    :param newlist: 存放处理好数据的列表
    :param oldlist: 存放未处理数据的列表
    :param union_list: 该列表是 处理的依据
    :return:
    '''
    for uitem in union_list:
        # print(f"{uitem['auxiliary_attribute_category_FName'] + '-------' + uitem['default_repository_FName']}")
        for aDitem in oldlist:
            # 外层循环全部结束才构造完毕 无需判重 因为 uitem 唯一
            if aDitem['auxiliary_attribute_category_FName'] and aDitem['default_repository_FName']:
                if aDitem['auxiliary_attribute_category_FName'] == uitem['auxiliary_attribute_category_FName'] \
                        and aDitem['default_repository_FName'] == uitem['default_repository_FName']:
                    newlist.append(aDitem)

    for uitem in union_list:
        # 添加残缺的数据
        for aDitem in oldlist:
            if aDitem not in newlist:
                if aDitem['auxiliary_attribute_category_FName'] == uitem['auxiliary_attribute_category_FName'] \
                        and aDitem['default_repository_FName'] == uitem['default_repository_FName']:
                    newlist.append(aDitem)


if __name__ == '__main__':
    # 初始工作
    dir = os.getcwd()
    xlsx, table_data = initData(dir + './开发部__面试__题目.xlsx', "分类数据")
    # 根据列名(字段名称)获取相应序号
    auxiliary_attribute_category_FName_index = getColumnIndex(table_data, '辅助属性类别_FName')
    default_repository_FName_index = getColumnIndex(table_data, '默认仓库_FName')

    # 根据列索引获得去重属性列表
    auxiliary_attribute_category_FName_list = getNoReppetList(table_data, auxiliary_attribute_category_FName_index)
    default_repository_FName_list = getNoReppetList(table_data, default_repository_FName_index)

    # 构造二合一列表(两个属性)
    union_list = get_unionlist(auxiliary_attribute_category_FName_list, default_repository_FName_list)
    # 构造所有数据列表
    allData_list = getAllDatalist(table_data)
    print(len(allData_list))
    # 构造新的数据列表
    newData_list = [allData_list[0]]  # 第一行元素是字段
    getnewData_list(newData_list, allData_list, union_list)

    print(len(newData_list))  # 新数据总条数
    write_excel_xls(newData_list, '整理后的数据', 'new.xlsx')
