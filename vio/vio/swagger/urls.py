# Copyright (c) 2017 VMware, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:

#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

from vio.swagger.views import SwaggerJsonView
from vio.swagger.views import ListTenantsView

urlpatterns = [
    url(r'^openoapi/multivim-vio/v1/swagger.json$', SwaggerJsonView.as_view()),
    url(r'^openoapi/multivim-vio/v1/(?P<vimid>[0-9a-zA-Z_-]+)/tenants$', ListTenantsView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
