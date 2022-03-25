import yaml

class YamlParse:
    encoding = 'utf-8'
    json = None

    def loadyaml(self, yamlfile = None):
        if yamlfile is None:
            print("未指定文件")
        try:
            file = open(yamlfile, 'r', encoding=self.encoding)
            self.json = yaml.load(file,Loader=yaml.FullLoader)
        except IOError as e:
            print(e)
        finally:
            if file is not None:
                file.close()

    def getJson(self):
        return self.json
