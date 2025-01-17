# Copyright 2016 The Kubernetes Authors.
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

from kubernetes import client, config


def main():
    # Configs can be set in Configuration class directly or using helper
    # utility. If no argument provided, the config will be loaded from
    # default location.
    config.load_kube_config()

    v1 = client.CoreV1Api()
    print("Listing all POD names, their IP and current state:")
    pods = obj.list_namespaced_pod()
    for pod in pods:
        print('Name of the pod is: %s' % pod.metadata.name)
        print('IP assigned to the pod is: %s' % pod.status.pod_ip)
        print('State of the pod is: %s' % pod.status.phase)


if __name__ == '__main__':
    main()
