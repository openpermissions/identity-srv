# -*- coding: utf-8 -*-
# Copyright 2016 Open Permissions Platform Coalition
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License. You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software distributed under the License is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.

import uuid
import time

start = time.time()
n = 10000
for i in range(n):
    uuid.uuid5(uuid.uuid1(), uuid.uuid4().urn)
end = time.time()
diff = end - start
print("It took {} to generate {} UUID5 based on UUId1 and UUID4.urn."
      "Avg time to gen one UUID: {}".format(diff, n, diff / n))

start = time.time()
n = 50000
for i in range(n):
    uuid.uuid5(uuid.uuid1(), uuid.uuid4().urn)
end = time.time()
diff = end - start
print("It took {} to generate {} UUID5 based on UUId1 and UUID4.urn."
      "Avg time to gen one UUID: {}".format(diff, n, diff / n))

start = time.time()
n = 100000
for i in range(n):
    uuid.uuid5(uuid.uuid1(), uuid.uuid4().urn)
end = time.time()
diff = end - start
print("It took {} to generate {} UUID5 based on UUId1 and UUID4.urn."
      "Avg time to gen one UUID: {}".format(diff, n, diff / n))

start = time.time()
n = 10000
for i in range(n):
    uuid.uuid3(uuid.uuid1(), uuid.uuid4().urn)
end = time.time()
diff = end - start
print("It took {} to generate {} UUID3 based on UUId1 and UUID4.urn."
      "Avg time to gen one UUID: {}".format(diff, n, diff / n))

start = time.time()
n = 50000
for i in range(n):
    uuid.uuid3(uuid.uuid1(), uuid.uuid4().urn)
end = time.time()
diff = end - start
print("It took {} to generate {} UUID3 based on UUId1 and UUID4.urn."
      "Avg time to gen one UUID: {}".format(diff, n, diff / n))

start = time.time()
n = 100000
for i in range(n):
    uuid.uuid3(uuid.uuid1(), uuid.uuid4().urn)
end = time.time()
diff = end - start
print("It took {} to generate {} UUID3 based on UUId1 and UUID4.urn."
      "Avg time to gen one UUID: {}".format(diff, n, diff / n))

start = time.time()
n = 10000
for i in range(n):
    uuid.uuid1()
end = time.time()
diff = end - start
print("It took {} to generate {} UUID1."
      "Avg time to gen one UUID: {}".format(diff, n, diff / n))

start = time.time()
n = 50000
for i in range(n):
    uuid.uuid1()
end = time.time()
diff = end - start
print("It took {} to generate {} UUID1."
      "Avg time to gen one UUID: {}".format(diff, n, diff / n))

start = time.time()
n = 100000
for i in range(n):
    uuid.uuid1()
end = time.time()
diff = end - start
print("It took {} to generate {} UUID1."
      "Avg time to gen one UUID: {}".format(diff, n, diff / n))

start = time.time()
n = 10000
for i in range(n):
    uuid.uuid4()
end = time.time()
diff = end - start
print("It took {} to generate {} UUID4."
      "Avg time to gen one UUID: {}".format(diff, n, diff / n))

start = time.time()
n = 50000
for i in range(n):
    uuid.uuid4()
end = time.time()
diff = end - start
print("It took {} to generate {} UUID4."
      "Avg time to gen one UUID: {}".format(diff, n, diff / n))

start = time.time()
n = 100000
for i in range(n):
    uuid.uuid4()
end = time.time()
diff = end - start
print("It took {} to generate {} UUID4."
      "Avg time to gen one UUID: {}".format(diff, n, diff / n))
