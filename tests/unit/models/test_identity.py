# -*- coding: utf-8 -*-
# Copyright 2016 Open Permissions Platform Coalition
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License. You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software distributed under the License is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.

import pytest

from identity.models.identity import validate, options


def setup_module(module):
    options.define('max_id_generation_count', default=1024)


def test_validate_passes_with_count():
    body = {"resolver_id": "https://r1234",
            "repository_id": "37cd1397e0814e989fa22da6b15fec60",
            "count": 2}
    result, errors = validate(body)
    assert not errors
    assert result == body


def test_validate_passes_without_count():
    body = {"resolver_id": "https://r1234",
            "repository_id": "37cd1397e0814e989fa22da6b15fec60"}
    result, errors = validate(body)
    assert not errors
    assert result['count'] == 1


def test_validate_empty_data():
    result, errors = validate({})
    assert errors


@pytest.mark.parametrize("body", [
    {"resolver_id": "https://r1234",
     "repository_id": "37cd1397e0814e989fa22da6b15fec60",
     "count": 2000},
    {"resolver_id": "https://r1234",
     "repository_id": "37cd1397e0814e989fa22da6b15fec60",
     "illegal": "x"},
    {"resolver_id": "r1234",
     "repository_id": "37cd1397e0814e989fa22da6b15fec60",
     },
    {"resolver_id": "https://r1234",
     "repository_id": "xyz",
     }
])
def test_validate_fails_on_one_error(body):
    result, errors = validate(body)
    assert len(errors) == 1


def test_multiple_invalid():
    body = {"resolver_id": "r1234",
            "repository_id": "xyz",
            "count": 2000,
            "illegal": "x"}
    result, errors = validate(body)
    assert len(errors) == 4
