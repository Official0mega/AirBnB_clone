#!/usr/bin/python3
"""
This module provides functionality for web application deployment using Fabric.
"""

import os
from datetime import datetime
from fabric.api import local, runs_once


@runs_once
def do_pack():
    """
    Archives the static files.

    This function creates a compressed archive of the web_static directory
    and stores it in the versions directory with a timestamp in the filename.
    Returns the path to the created archive file.
    """
    # Create the versions directory if it doesn't exist
    if not os.path.isdir("versions"):
        os.mkdir("versions")

    # Get the current date and time
    cur_time = datetime.now()

    # Define the output filename with a timestamp
    output = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        cur_time.year,
        cur_time.month,
        cur_time.day,
        cur_time.hour,
        cur_time.minute,
        cur_time.second
    )

    try:
        # Compress the web_static directory using the tar command
        print("Packing web_static to {}".format(output))
        local("tar -cvzf {} web_static".format(output))

        # Get the size of the created archive
        archive_size = os.stat(output).st_size

        # Print a success message with archive details
        print("web_static packed: {} -> {} Bytes".format(output, archive_size))
    except Exception:
        # Handle exceptions by setting output to None
        output = None

    return output
