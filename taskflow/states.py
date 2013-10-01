# -*- coding: utf-8 -*-

# vim: tabstop=4 shiftwidth=4 softtabstop=4

#    Copyright (C) 2012 Yahoo! Inc. All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

# Job states.
CLAIMED = 'CLAIMED'
FAILURE = 'FAILURE'
PENDING = 'PENDING'
RUNNING = 'RUNNING'
SUCCESS = 'SUCCESS'
UNCLAIMED = 'UNCLAIMED'

# Flow states.
FAILURE = FAILURE
PENDING = 'PENDING'
REVERTING = 'REVERTING'
REVERTED = 'REVERTED'
RUNNING = RUNNING
SUCCESS = SUCCESS
SUSPENDING = 'SUSPENDING'
SUSPENDED = 'SUSPENDED'

# Task states.
FAILURE = FAILURE
SUCCESS = SUCCESS
REVERTED = REVERTED
REVERTING = REVERTING

# TODO(harlowja): use when we can timeout tasks??
TIMED_OUT = 'TIMED_OUT'
