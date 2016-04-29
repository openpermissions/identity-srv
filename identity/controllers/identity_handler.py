# -*- coding: utf-8 -*-
# Copyright 2016 Open Permissions Platform Coalition
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License. You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software distributed under the License is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.

"""All Handler for ID related requests
"""
from tornado.escape import json_decode
from koi.base import BaseHandler
from koi import exceptions
from bass.hubkey import generate_hub_key

from identity.models.identity import validate


class IdentityHandler(BaseHandler):
    """Super class for handling identity asset
    """

    def post(self, entity_type):
        """Can return as many IDs as configured via max_id_generation_count
        Return a HTTP response with a JSON containing a list of generated IDs
        or a 400 with appropriate error message if invalid param was provided.
        """

        if self.request.body:
            body = json_decode(self.request.body)
        else:
            body = {}

        result, errors = validate(body)
        if errors:
            raise exceptions.HTTPError(400, errors)

        hub_keys = [generate_hub_key(result['resolver_id'],
                                     result['hub_id'],
                                     result['repository_id'],
                                     entity_type)
                   for _ in range(result['count'])]
        self.finish({'status': 200, 'data': hub_keys})
