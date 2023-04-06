#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the
contents of the web_static folder of your AirBnB
Clone repo, using the function do_pack
"""

from fabric.api import local
from os.path import isdir
from datetime import datetime


def do_pack():
    """ Generates a .tgz archive from the web_static """
    try:
        date_time = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_path = "versions/web_static_{}.tgz".format(date_time)
        local("tar -cvzf {} web_static".format(file_path))
        return file_path
    except:
        return None
