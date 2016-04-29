# -*- coding: utf-8 -*-
# Copyright 2016 Open Permissions Platform Coalition
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License. You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software distributed under the License is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.


import re
from setuptools import find_packages, setup

with open('identity/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

setup(
    name='open permssions platform identity service',
    version=version,
    description='Open Permissions Platform Coalition Identity Service',
    author='CDE Catapult',
    author_email='support-copyrighthub@cde.catapult.org.uk',
    url='https://github.com/openpermissions/identity-srv',
    packages=find_packages(exclude=['test']),
    entry_points={
        'console_scripts':
            ['open-permissions-platform-identity-svr = identity.app:main']},
    )
