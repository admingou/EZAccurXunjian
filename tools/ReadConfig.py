from flask import current_app
import os
import yaml


class ReadConf:
    """
    配置读取
    """
    encode = "utf-8"
    conf_json = ""
    def __init__(self):
         self.path = os.path.join(current_app.root_path, "conf/conf.yaml")


    def LoadConf(self):
        """
        加载yaml配置文件
        :return:
        """
        try:
            with open(self.path, "r", encoding=self.encode) as f:
                self.conf_json = yaml.load(f, Loader=yaml.FullLoader)
        except Exception as e:
             raise e


    def GetConf(self):
        """
        获取yaml读取结果
        :return: yaml解析内容
        """
        return self.conf_json