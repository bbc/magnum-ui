#  Copyright 2015 Cisco Systems
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

from django.utils.translation import gettext_lazy as _
import horizon

# DO NOT REMOVE
# This needs for register url of REST API.
# Dashboard plugins load REST API from here.
from magnum_ui.api.rest import magnum  # noqa: F401


class Clusters(horizon.Panel):
    name = _("Clusters")
    slug = "clusters"
