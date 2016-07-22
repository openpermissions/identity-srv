# -*- coding: utf-8 -*-
# Copyright 2016 Open Permissions Platform Coalition
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License. You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software distributed under the License is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.

"""Identity data validation
"""
from voluptuous import (
    Schema, Required, Optional, MultipleInvalid, All, Range, Match,
    MatchInvalid, RequiredFieldInvalid)
from tornado.options import options
from bass.hubkey import PARTS


def _match_part(part):
    message = "Field '{}' does not match regular expression '{}'"
    return Match(PARTS[part], message.format(part, PARTS[part]))


def schema():
    """
    returns a volupuous Schema object for validating
    """
    schema = {Required(part): _match_part(part) for part
              in ['resolver_id', 'repository_id']}
    schema[Optional('count', default=1)] = All(
        int, Range(min=1, max=options.max_id_generation_count))
    return Schema(schema, required=True)


def _format_error(error):
    if isinstance(error, MatchInvalid):
        errors = [error.error_message for _ in error.path]
    elif isinstance(error, RequiredFieldInvalid):
        errors = ["Missing '{}'".format(p) for p in error.path]
    elif error.error_message == 'extra keys not allowed':
        errors = ["Unexpected field '{}'".format(p) for p in error.path]
    else:
        errors = ["Field '{}' {}".format(p, error.error_message)
                  for p in error.path]
    return errors


def validate(data):
    """
    validate the data for hub key generation
    :param data: a dictionary
    :returns: a dictionary for result and list for errors
    """
    result, errors = None, []
    try:
        result = schema()(data)
    except MultipleInvalid as e:
        for error in e.errors:
            errors += _format_error(error)
    return result, sorted(errors)
