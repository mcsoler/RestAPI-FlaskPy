import re
import subprocess
import sys
import os
import psutil

class GProcess:
    def __init__(self, one_process = False):
        ''' Constructor for this class. '''
        self.process_name = ''
        self.one_process = one_process
        self.pid = os.getpid()

    def runCmd(self, cmds = ['cat','/dev/null'], shell_flag=False):
        if self.one_process:
            if self.is_running([x for x in cmds if x != "|" and x != "'" and x != '"']):
                print("Process alredy running ")
                return False

        p = None
        if shell_flag:
            p = subprocess.check_output(' '.join(cmds), shell=shell_flag)
        else:
            p = subprocess.check_output(cmds, shell=shell_flag)
        rearr =  p.splitlines()
        out = ""
        for lineb in rearr:
            line = lineb.decode('utf-8')
            out += line + "\n"
            #print(line)
        return out

    def runAsProcess(self, cmds = ['cat','/dev/null'], shell_flag=False):
        print(self.pid)
        if self.one_process:
            if self.is_running([x for x in cmds if x != "|" and x != "'" and x != '"']):
                print("Process alredy running ")
                return False

        if shell_flag:
            p = subprocess.Popen(' '.join(cmds), stdout=sys.stdout, stderr=sys.stdout, shell=shell_flag)
        else:
            p = subprocess.Popen(cmds, stdout=sys.stdout, stderr=sys.stdout, shell=shell_flag)

    def is_running(self, match_strs = [], nomatch_strs = []):
        cmd = "ps -ef | grep -v grep "
        for s in match_strs:
            if s.replace(' ','') != '':
                cmd += " | grep " + s
        for s in nomatch_strs:
            if s.replace(' ','') != '':
                cmd += " | grep -v " + s

        #print(cmd)
        try:
            res = subprocess.check_output(cmd, shell=True)
            lines = res.splitlines()
            if len(lines) > 0:
                for lb in lines:
                    l = lb.decode('utf-8')
                    pflds = l.split()
                    if int(pflds[1]) != self.pid:
                        return True
                return False
            else:
                return False
        except:
            return False

    def exists(self):
        if os.pid_exists(self.pid):
            return True
        else:
            return False

    def run_watch_dog(self, process_type = ""):
        wd_cmd = "./root/scripts/dev/gprocess_watchdog.py " + str(self.pid) + " " + process_type
        os.system(wd_cmd + " &")
