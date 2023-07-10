#!/usr/bin/python3
"""
This script provides utility functions for testing the AirBnb clone modules.
"""

import os
from typing import TextIO
from models.engine.file_storage import FileStorage


def clear_stream(stream: TextIO):
    """
    Clears the contents of a given stream.

    Args:
        stream (TextIO): The stream to clear.
    """
    if stream.seekable():
        stream.seek(0)  # Reset the stream position to the beginning
        stream.truncate(0)  # Truncate the stream to remove all data


def delete_file(file_path: str):
    """
    Deletes a file if it exists.

    Args:
        file_path (str): The path of the file to delete.
    """
    if os.path.isfile(file_path):
        os.unlink(file_path)  # Remove the file from the file system


def reset_store(store: FileStorage, file_path='file.json'):
    """
    Resets the items in the given store.

    Args:
        store (FileStorage): The FileStorage to reset.
        file_path (str): The path to the store's file.
    """
    with open(file_path, mode='w') as file:
        file.write('{}')  # Write an empty dictionary to the file
    if store is not None:
        store.reload()  # Reload the store to reflect the changes


def read_text_file(file_name):
    """
    Reads the contents of a given file.

    Args:
        file_name (str): The name of the file to read.

    Returns:
        str: The contents of the file if it exists.
    """
    lines = []
    if os.path.isfile(file_name):
        with open(file_name, mode='r') as file:
            for line in file.readlines():
                lines.append(line)  # Append each line to the list
    return ''.join(lines)  # Join the lines into a single string


def write_text_file(file_name, text):
    """
    Writes a text to a given file.

    Args:
        file_name (str): The name of the file to write to.
        text (str): The content of the file.
    """
    with open(file_name, mode='w') as file:
        file.write(text)  # Write the text to the file


# Utility functions for testing modules in the Airbnb clone application

