#
# Copyright 2012 Quantopian, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.



from utils.protocol_utils import Enum

# Datasource type should completely determine the other fields of a
# message with its type.
DATASOURCE_TYPE = Enum(
    'AS_TRADED_EQUITY',
    'MERGER',
    'SPLIT',
    'DIVIDEND',
    'TRADE',
    'EMPTY',
    'DONE'
)


class Event(object):

    def __init__(self, initial_values=None):
        if initial_values:
            self.__dict__ = initial_values

    def __getitem__(self, name):
        return getattr(self, name)

    def __setitem__(self, name, value):
        setattr(self, name, value)

    def __delitem__(self, name):
        delattr(self, name)

    def keys(self):
        return self.__dict__.keys()

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __contains__(self, name):
        return name in self.__dict__

    def __repr__(self):
        return "Event({0})".format(self.__dict__)


class Portfolio(object):

    def __init__(self, initial_values=None):
        if initial_values:
            self.__dict__ = initial_values

    def __repr__(self):
        return "Portfolio({0})".format(self.__dict__)


class Position(object):

    def __init__(self, sid):
        self.sid = sid
        self.amount = 0
        self.cost_basis = 0.0  # per share
        self.last_sale_price = 0.0

    def __repr__(self):
        return "Position({0})".format(self.__dict__)


class Positions(dict):

    def __missing__(self, key):
        pos = Position(key)
        self[key] = pos
        return pos
