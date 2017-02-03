# -*- coding: utf-8 -*-

# Imports ###########################################################

import os
from setuptools import setup


# Functions #########################################################

def package_data(pkg, root_list):
    """Generic function to find package_data for `pkg` under `root`."""
    data = []
    for root in root_list:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


# Main ##############################################################

setup(
    name='xblock-drag-and-drop-v2-fr',
    version='2.0.14',
    description='XBlock - Drag-and-Drop v2 FR',
    packages=['drag_and_drop_v2fr'],
    install_requires=[
        'XBlock',
        'xblock-utils',
        'ddt',
        'mock',
    ],
    entry_points={
        'xblock.v1': 'drag-and-drop-v2fr = drag_and_drop_v2fr:DragAndDropFrBlock',
    },
    package_data=package_data("drag_and_drop_v2fr", ["static", "templates", "public", "translations"]),
)
