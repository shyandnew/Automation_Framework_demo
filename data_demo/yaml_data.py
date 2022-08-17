'''
操作yaml文件类实现
'''

import yaml

class OperationYaml:

    def get_yaml(self, path):
        with open(path, encoding='utf-8') as f:
            #return yaml.safe_load(f.read())
            return yaml.load(f.read(), Loader=yaml.FullLoader)

    def get_yamls(self, path):
        with open(path, encoding='utf-8') as f:
            return yaml.load_all(f.read(), Loader=yaml.FullLoader)