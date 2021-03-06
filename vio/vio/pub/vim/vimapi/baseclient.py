# Copyright (c) 2017 VMware, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

import logging

from vio.pub.vim.drivers import vimdriver as driver_base

LOG = logging.getLogger(__name__)


class baseclient(object):

    def __init__(self,  **kwargs):
        # initialize clients
        self._identityclient = None
        self._glanceclient = None
        self._computeClient = None
        self._cinderclient = None

    def identity(self, data):
        '''Construct compute client based on object.

        :param obj: Object for which the client is created. It is expected to
                    be None when retrieving an existing client. When creating
                    a client, it contains the user and project to be used.
        '''

        if self._identityclient is not None:
            return self._identityclient
        self._identityclient = driver_base.VimDriver().identity(data)
        return self._identityclient

    def glance(self, data):
        if self._glanceclient is not None:
            return self._glanceclient
        self._glanceclient = driver_base.VimDriver().glance(data)
        return self._glanceclient

    def compute(self, data):
        if self._computeClient is not None:
            return self._computeClient

        self._computeClient = driver_base.VimDriver().compute(data)
        return self._computeClient

    def cinder(self, data):
        if self._cinderclient is not None:
            return self._cinderclient

        self._cinderclient = driver_base.VimDriver().cinder(data)
        return self._cinderclient
