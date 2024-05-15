import re
import yaml
import os

class Config:
    def __init__(self):
        ''' Constructor for this class. '''
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.config_file = dir_path + "/config_clt.yml"
        self.config = {}
        self.cnf_local = {}
        self.loc = ""
        self.env = "" # prod or dev
        self.load()

    def load(self):
        f = open(self.config_file,'r')
        self.config = yaml.safe_load(f)

    def get(self,param):
        par = self.config.get(param,"")
        if par is None:
            return ""
        else:
            return par

    def get_key_match(self, match):
        return [ param for param in self.config.keys() if match in param ]
