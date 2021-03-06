# Copyright 2019 Extreme Networks, Inc.
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

import six

from st2common.runners.base_action import Action


class PacksTransformationAction(Action):
    def run(self, packs_status):
        """
        :param packs_status: Result from packs.download action.
        :type: packs_status: ``dict``
        """
        packs = []
        for pack_name, status in six.iteritems(packs_status):
            if 'success' in status.lower():
                packs.append(pack_name)
        return packs
