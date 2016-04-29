# -*- coding: utf-8 -*-
# Copyright 2016 Open Permissions Platform Coalition
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License. You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software distributed under the License is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.

from mock import MagicMock, patch
from identity.controllers.capabilities_handler import CapabilitiesHandler
from tornado.escape import json_encode


@patch('identity.controllers.capabilities_handler.options')
def test_get_capabilities(options):
    options.max_id_generation_count = 1024
    caps = CapabilitiesHandler(MagicMock(), MagicMock())
    caps.finish = MagicMock()

    # MUT
    caps.get()
    msg = {"max_id_generation_count":
           "{}".format(options.max_id_generation_count)}

    caps.finish.assert_called_once_with({'status': 200, 'data': msg})
