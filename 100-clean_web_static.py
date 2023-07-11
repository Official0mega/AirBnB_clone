#!/usr/bin/python3
"""
A module for web application deployment with Fabric.
"""

import os
from datetime import datetime
from fabric.api import env, local, put, run, runs_once


env.hosts = ["34.73.0.174", "35.196.78.105"]
"""
The list of host server IP addresses.

This variable sets the host servers where the static files will be deployed.
"""


@runs_once
def do_pack():
    """
    Archives the static files.

    This function creates a compressed archive of the web_static directory
    and stores it in the versions directory with a timestamp in the filename.
    Returns the path to the created archive file.
    """
    # Create versions directory if it doesn't exist
    if not os.path.isdir("versions"):
        os.mkdir("versions")

    # Get current date and time
    cur_time = datetime.now()

    # Define the output filename with timestamp
    output = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        cur_time.year,
        cur_time.month,
        cur_time.day,
        cur_time.hour,
        cur_time.minute,
        cur_time.second
    )

    try:
        # Compress web_static directory using tar command
        print("Packing web_static to {}".format(output))
        local("tar -cvzf {} web_static".format(output))

        # Get the size of the created archive
        archive_size = os.stat(output).st_size

        # Print success message with archive details
        print("web_static packed: {} -> {} Bytes".format(output, archive_size))
    except Exception:
        # Handle exceptions by setting output to None
        output = None

    return output


def do_deploy(archive_path):
    """
    Deploys the static files to the host servers.

    Args:
        archive_path (str): The path to the archived static files.
    """
    if not os.path.exists(archive_path):
        return False

    file_name = os.path.basename(archive_path)
    folder_name = file_name.replace(".tgz", "")
    folder_path = "/data/web_static/releases/{}/".format(folder_name)
    success = False

    try:
        put(archive_path, "/tmp/{}".format(file_name))
        run("mkdir -p {}".format(folder_path))
        run("tar -xzf /tmp/{} -C {}".format(file_name, folder_path))
        run("rm -rf /tmp/{}".format(file_name))
        run("mv {}web_static/* {}".format(folder_path, folder_path))
        run("rm -rf {}web_static".format(folder_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder_path))
        print('New version deployed!')
        success = True
    except Exception:
        success = False

    return success


def deploy():
    """
    Archives and deploys the static files to the host servers.
    """
    archive_path = do_pack()
    return do_deploy(archive_path) if archive_path else False


def do_clean(number=0):
    """
    Deletes out-of-date archives of the static files.

    Args:
        number (int): The number of archives to keep.
    """
    archives = os.listdir('versions/')
    archives.sort(reverse=True)
    start = int(number)
    if not start:
        start += 1
    if start < len(archives):
        archives = archives[start:]
    else:
        archives = []
    for archive in archives:
        os.unlink('versions/{}'.format(archive))
    cmd_parts = [
        "rm -rf $(",
        "find /data/web_static/releases/ -maxdepth 1 -type d -iregex",
        " '/data/web_static/releases/web_static_.*'",
        " | sort -r | tr '\\n' ' ' | cut -d ' ' -f{}-)".format(start + 1)
    ]
    run(''.join(cmd_parts))
