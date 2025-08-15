#
# Copyright 2025 AOSC Developers
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
#
# Requires Python 2.6+ and Openssl 1.0+
#

import azurelinuxagent.common.utils.shellutil as shellutil
from azurelinuxagent.common.osutil.default import DefaultOSUtil


class AoscOSUtil(DefaultOSUtil):

    def __init__(self):
        super(AoscOSUtil, self).__init__()
        self.jit_enabled = True
    
    @staticmethod
    def get_systemd_unit_file_install_path():
        return "/usr/lib/systemd/system"
    
    @staticmethod
    def get_agent_bin_path():
        return "/usr/bin"

    def restart_ssh_service(self):
        return shellutil.run("systemctl --job-mode=ignore-dependencies try-reload-or-restart sshd", chk_err=False)

    def stop_agent_service(self):
        return shellutil.run("systemctl stop {0}".format(self.service_name), chk_err=False)

    def start_agent_service(self):
        return shellutil.run("systemctl start {0}".format(self.service_name), chk_err=False)

    def start_network(self):
        pass

    def remove_rules_files(self, rules_files=""):
        pass

    def restore_rules_files(self, rules_files=""):
        pass

    def get_dhcp_lease_endpoint(self):
        return self.get_endpoint_from_leases_path('/var/lib/NetworkManager/*.lease')

    def is_dhcp_enabled(self):
        return True

    def conf_sshd(self, disable_password):
        # Use the default implementation which works with systemd
        super(AoscOSUtil, self).conf_sshd(disable_password)
