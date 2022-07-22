import os
import sys
import shutil
import subprocess
input = sys.stdin.readline

if __name__=="__main__":
    contest_name = input().rstrip()

    if os.path.exists(contest_name): exit()
    else: os.mkdir(contest_name)
    shutil.copy("template.py", contest_name+"/"+contest_name+"_a.py")
    shutil.copy("template.py", contest_name+"/"+contest_name+"_b.py")
    shutil.copy("template.py", contest_name+"/"+contest_name+"_c.py")
    shutil.copy("template.py", contest_name+"/"+contest_name+"_d.py")
