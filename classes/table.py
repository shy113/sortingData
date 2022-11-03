# *-* encoding:utf8 *_*
# Author       : GZH
# Date         : 2022年10月28日
# Description  : hahahhahaha

# 产品属性类
class Product:
    def __init__(self, arg):
        # self.code = Node # 代码
        # self.name = None  # 名称
        # self.material_full_name = None  # 物料全名
        # self.specifications = None  # 规格型号
        # self.auxiliary_attribute_category_FName = None  # 辅助属性类别_FName
        # self.auxiliary_attribute_category_FNumber = None  # 辅助属性类别_FNumber
        # self.material_properties_FName = None  # 物料属性_FName
        # self.default_repository_FName = None  # 默认仓库_FName
        # self.default_repository_FNumber = None  # 默认仓库_FNumber
        # self.Source_FName = None  # 来源_FName

        self.code, self.name, self.material_full_name, self.specifications, self.auxiliary_attribute_category_FName, \
        self.auxiliary_attribute_category_FNumber, self.material_properties_FName, self.default_repository_FName, \
        self.default_repository_FNumber, self.Source_FName = arg
        self.featureId = None  # 新增一个特征id 待会用来排序

    # 将表中每一行数据转成字典
    def getObjToDict(self):
        dict = {
            'code': self.code,
            'name': self.name,
            'material_full_name': self.material_full_name,
            'specifications': self.specifications,
            'auxiliary_attribute_category_FName': self.auxiliary_attribute_category_FName,
            'auxiliary_attribute_category_FNumber': self.auxiliary_attribute_category_FNumber,
            'material_properties_FName': self.material_properties_FName,
            'default_repository_FName': self.default_repository_FName,
            'default_repository_FNumber': self.default_repository_FNumber,
            'Source_FName': self.Source_FName,
        }
        return dict

    def getObjToList(self):
        list = []
        dict = self.getObjToDict()
        for k, v in dict.items():
            list.append(v)
        return list

    def getFeatureDict(self):
        dict = {
            'auxiliary_attribute_category_FName': self.auxiliary_attribute_category_FName,
            'default_repository_FName': self.default_repository_FName
        }
        return dict


# 分类依据类
class Feature:
    def __init__(self, arg):
        self.auxiliary_attribute_category_FName, self.default_repository_FName = arg

    def getObjToDict(self):
        dict = {
            'auxiliary_attribute_category_FName': self.auxiliary_attribute_category_FName,
            'default_repository_FName': self.default_repository_FName
        }
        return dict
