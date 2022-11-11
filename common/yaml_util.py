import os
import yaml


class YamlUtil:
    # 读取yml文件
    def read_extract_yaml(self, key):
        with open(os.getcwd()+"/extract.yml", mode='r', encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value[key]

    # 向yml文件写入数据
    def write_excract_yaml(self, data):
        with open(os.getcwd()+"/extract.yml", mode='w', encoding='utf-8') as f:
            yaml.dump(data=data, stream=f, allow_unicode=True)

    # 清除yml文件
    def clear_excract_yaml(self):
        with open(os.getcwd() + "/extract.yml", mode='w', encoding='utf-8') as f:
            f.truncate()

    def read_tesecase_yaml(self, yaml_name):
        with open(os.getcwd() +"/testcases/"+ yaml_name, mode='r', encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value