# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi import util


class KubernetesServiceConnectionRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, local: bool=None, kubeconfig: object=None, verify_ssl: bool=None):
        """KubernetesServiceConnectionRequest - a model defined in OpenAPI

        :param name: The name of this KubernetesServiceConnectionRequest.
        :param local: The local of this KubernetesServiceConnectionRequest.
        :param kubeconfig: The kubeconfig of this KubernetesServiceConnectionRequest.
        :param verify_ssl: The verify_ssl of this KubernetesServiceConnectionRequest.
        """
        self.openapi_types = {
            'name': str,
            'local': bool,
            'kubeconfig': object,
            'verify_ssl': bool
        }

        self.attribute_map = {
            'name': 'name',
            'local': 'local',
            'kubeconfig': 'kubeconfig',
            'verify_ssl': 'verify_ssl'
        }

        self._name = name
        self._local = local
        self._kubeconfig = kubeconfig
        self._verify_ssl = verify_ssl

    @classmethod
    def from_dict(cls, dikt: dict) -> 'KubernetesServiceConnectionRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The KubernetesServiceConnectionRequest of this KubernetesServiceConnectionRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this KubernetesServiceConnectionRequest.


        :return: The name of this KubernetesServiceConnectionRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this KubernetesServiceConnectionRequest.


        :param name: The name of this KubernetesServiceConnectionRequest.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")

        self._name = name

    @property
    def local(self):
        """Gets the local of this KubernetesServiceConnectionRequest.

        If enabled, use the local connection. Required Docker socket/Kubernetes Integration

        :return: The local of this KubernetesServiceConnectionRequest.
        :rtype: bool
        """
        return self._local

    @local.setter
    def local(self, local):
        """Sets the local of this KubernetesServiceConnectionRequest.

        If enabled, use the local connection. Required Docker socket/Kubernetes Integration

        :param local: The local of this KubernetesServiceConnectionRequest.
        :type local: bool
        """

        self._local = local

    @property
    def kubeconfig(self):
        """Gets the kubeconfig of this KubernetesServiceConnectionRequest.

        Paste your kubeconfig here. authentik will automatically use the currently selected context.

        :return: The kubeconfig of this KubernetesServiceConnectionRequest.
        :rtype: object
        """
        return self._kubeconfig

    @kubeconfig.setter
    def kubeconfig(self, kubeconfig):
        """Sets the kubeconfig of this KubernetesServiceConnectionRequest.

        Paste your kubeconfig here. authentik will automatically use the currently selected context.

        :param kubeconfig: The kubeconfig of this KubernetesServiceConnectionRequest.
        :type kubeconfig: object
        """

        self._kubeconfig = kubeconfig

    @property
    def verify_ssl(self):
        """Gets the verify_ssl of this KubernetesServiceConnectionRequest.

        Verify SSL Certificates of the Kubernetes API endpoint

        :return: The verify_ssl of this KubernetesServiceConnectionRequest.
        :rtype: bool
        """
        return self._verify_ssl

    @verify_ssl.setter
    def verify_ssl(self, verify_ssl):
        """Sets the verify_ssl of this KubernetesServiceConnectionRequest.

        Verify SSL Certificates of the Kubernetes API endpoint

        :param verify_ssl: The verify_ssl of this KubernetesServiceConnectionRequest.
        :type verify_ssl: bool
        """

        self._verify_ssl = verify_ssl
