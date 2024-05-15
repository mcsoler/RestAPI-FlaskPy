import re

from .Config import Config
import json
import yaml
import subprocess
import sys

class APICursor:
    def __init__(self):
        ''' Constructor for this class. '''
        self.rowcount = 0
        self.rows = []

class Api:
    def __init__(self):
        ''' Constructor for this class. '''
        self.cnf = Config()
        self.api_url = self.cnf.get('backend_api_url')
        self.cursor = APICursor()

    def get(self, cmd):
        try:
            out = subprocess.check_output(cmd, shell=True)
            return out.decode('utf8')
        except:
            print("Error sending HB command ", sys.exc_info()[0])
            pass
        return None

    def get_current_operation(self):
        """

        """
        cmd = "curl -s -X POST -H \"Content-type: application/json\"  -d '{\"backend_api_key\": \""+self.cnf.get('backend_api_key')+"\",\"sql\": \"select * from CM_CURRENT_OPERATION\"}' _APIURL_/db_sql"

        cmd_s = cmd.replace('_APIURL_', self.api_url)
        #print(cmd_s)
        return json.loads(self.get(cmd_s))
    

    def execute_sql(self, sql):
        """

        """
        sql = sql.replace('\\"', "'")
        cmd = "curl -s -H \"Content-type: application/json\" -X POST -d \"{\\\"backend_api_key\\\": \\\""+self.cnf.get('backend_api_key')+"\\\",\\\"sql\\\": \\\""+sql+"\\\"}\" _APIURL_/db_sql"
        cmd_s = cmd.replace('_APIURL_', self.api_url)
        print(cmd_s)
        o_str = {}
        try:
            o_str = json.loads(self.get(cmd_s))
            return o_str
        except Exception as e:
            print("Error: "+str(e))
            o_str = {'error': str(e)}
        if True:
            print(self.get(cmd_s))
            o_str = print(self.get(cmd_s))
            return o_str
        #except Exception as e:
        #    print("Error: "+str(e),o_str,cmd_s)
        #    o_str = {'error': str(e)}
        return o_str
        

    def run_agent(self, agent, args=[]):
        """

        """
        argstr = ''
        for i in range(0,len(args)):
            argstr += ',\"arg'+str(i)+'\": \"'+args[i] +'\"'
        cmd = "curl -s -H \"Content-type: application/json\" -X POST -d '{\"backend_api_key\": \""+self.cnf.get('backend_api_key')+"\",\"agent\": \""+agent+"\""+argstr+"}' _APIURL_/run_agent"
        cmd_s = cmd.replace('_APIURL_', self.api_url)
        print(cmd_s)

        return json.loads(self.get(cmd_s))
        #if cmd_s is None:
        #    sys.stderr.write("ERROR in API cmd: ",cmd_s)
        #    return json.loads({'results': []})
        #else:
        #    jin = json.loads(self.get(cmd_s))
        #    return jin
