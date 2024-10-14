# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi.models.denied_action_enum import DeniedActionEnum
from authentik_openapi.models.flow_designation_enum import FlowDesignationEnum
from authentik_openapi.models.flow_layout_enum import FlowLayoutEnum
from authentik_openapi.models.policy_engine_mode import PolicyEngineMode
import re
from authentik_openapi import util


class FlowSet(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, pk: str=None, policybindingmodel_ptr_id: str=None, name: str=None, slug: str=None, title: str=None, designation: FlowDesignationEnum=None, background: str=None, policy_engine_mode: PolicyEngineMode=None, compatibility_mode: bool=None, export_url: str=None, layout: FlowLayoutEnum=None, denied_action: DeniedActionEnum=None):
        """FlowSet - a model defined in OpenAPI

        :param pk: The pk of this FlowSet.
        :param policybindingmodel_ptr_id: The policybindingmodel_ptr_id of this FlowSet.
        :param name: The name of this FlowSet.
        :param slug: The slug of this FlowSet.
        :param title: The title of this FlowSet.
        :param designation: The designation of this FlowSet.
        :param background: The background of this FlowSet.
        :param policy_engine_mode: The policy_engine_mode of this FlowSet.
        :param compatibility_mode: The compatibility_mode of this FlowSet.
        :param export_url: The export_url of this FlowSet.
        :param layout: The layout of this FlowSet.
        :param denied_action: The denied_action of this FlowSet.
        """
        self.openapi_types = {
            'pk': str,
            'policybindingmodel_ptr_id': str,
            'name': str,
            'slug': str,
            'title': str,
            'designation': FlowDesignationEnum,
            'background': str,
            'policy_engine_mode': PolicyEngineMode,
            'compatibility_mode': bool,
            'export_url': str,
            'layout': FlowLayoutEnum,
            'denied_action': DeniedActionEnum
        }

        self.attribute_map = {
            'pk': 'pk',
            'policybindingmodel_ptr_id': 'policybindingmodel_ptr_id',
            'name': 'name',
            'slug': 'slug',
            'title': 'title',
            'designation': 'designation',
            'background': 'background',
            'policy_engine_mode': 'policy_engine_mode',
            'compatibility_mode': 'compatibility_mode',
            'export_url': 'export_url',
            'layout': 'layout',
            'denied_action': 'denied_action'
        }

        self._pk = pk
        self._policybindingmodel_ptr_id = policybindingmodel_ptr_id
        self._name = name
        self._slug = slug
        self._title = title
        self._designation = designation
        self._background = background
        self._policy_engine_mode = policy_engine_mode
        self._compatibility_mode = compatibility_mode
        self._export_url = export_url
        self._layout = layout
        self._denied_action = denied_action

    @classmethod
    def from_dict(cls, dikt: dict) -> 'FlowSet':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The FlowSet of this FlowSet.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pk(self):
        """Gets the pk of this FlowSet.


        :return: The pk of this FlowSet.
        :rtype: str
        """
        return self._pk

    @pk.setter
    def pk(self, pk):
        """Sets the pk of this FlowSet.


        :param pk: The pk of this FlowSet.
        :type pk: str
        """
        if pk is None:
            raise ValueError("Invalid value for `pk`, must not be `None`")

        self._pk = pk

    @property
    def policybindingmodel_ptr_id(self):
        """Gets the policybindingmodel_ptr_id of this FlowSet.


        :return: The policybindingmodel_ptr_id of this FlowSet.
        :rtype: str
        """
        return self._policybindingmodel_ptr_id

    @policybindingmodel_ptr_id.setter
    def policybindingmodel_ptr_id(self, policybindingmodel_ptr_id):
        """Sets the policybindingmodel_ptr_id of this FlowSet.


        :param policybindingmodel_ptr_id: The policybindingmodel_ptr_id of this FlowSet.
        :type policybindingmodel_ptr_id: str
        """
        if policybindingmodel_ptr_id is None:
            raise ValueError("Invalid value for `policybindingmodel_ptr_id`, must not be `None`")

        self._policybindingmodel_ptr_id = policybindingmodel_ptr_id

    @property
    def name(self):
        """Gets the name of this FlowSet.


        :return: The name of this FlowSet.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FlowSet.


        :param name: The name of this FlowSet.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def slug(self):
        """Gets the slug of this FlowSet.

        Visible in the URL.

        :return: The slug of this FlowSet.
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this FlowSet.

        Visible in the URL.

        :param slug: The slug of this FlowSet.
        :type slug: str
        """
        if slug is None:
            raise ValueError("Invalid value for `slug`, must not be `None`")
        if slug is not None and len(slug) > 50:
            raise ValueError("Invalid value for `slug`, length must be less than or equal to `50`")
        if slug is not None and not re.search(r'^[-a-zA-Z0-9_]+$', slug):
            raise ValueError("Invalid value for `slug`, must be a follow pattern or equal to `/^[-a-zA-Z0-9_]+$/`")

        self._slug = slug

    @property
    def title(self):
        """Gets the title of this FlowSet.

        Shown as the Title in Flow pages.

        :return: The title of this FlowSet.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this FlowSet.

        Shown as the Title in Flow pages.

        :param title: The title of this FlowSet.
        :type title: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")

        self._title = title

    @property
    def designation(self):
        """Gets the designation of this FlowSet.

        Decides what this Flow is used for. For example, the Authentication flow is redirect to when an un-authenticated user visits authentik.

        :return: The designation of this FlowSet.
        :rtype: FlowDesignationEnum
        """
        return self._designation

    @designation.setter
    def designation(self, designation):
        """Sets the designation of this FlowSet.

        Decides what this Flow is used for. For example, the Authentication flow is redirect to when an un-authenticated user visits authentik.

        :param designation: The designation of this FlowSet.
        :type designation: FlowDesignationEnum
        """
        if designation is None:
            raise ValueError("Invalid value for `designation`, must not be `None`")

        self._designation = designation

    @property
    def background(self):
        """Gets the background of this FlowSet.

        Get the URL to the background image. If the name is /static or starts with http it is returned as-is

        :return: The background of this FlowSet.
        :rtype: str
        """
        return self._background

    @background.setter
    def background(self, background):
        """Sets the background of this FlowSet.

        Get the URL to the background image. If the name is /static or starts with http it is returned as-is

        :param background: The background of this FlowSet.
        :type background: str
        """
        if background is None:
            raise ValueError("Invalid value for `background`, must not be `None`")

        self._background = background

    @property
    def policy_engine_mode(self):
        """Gets the policy_engine_mode of this FlowSet.


        :return: The policy_engine_mode of this FlowSet.
        :rtype: PolicyEngineMode
        """
        return self._policy_engine_mode

    @policy_engine_mode.setter
    def policy_engine_mode(self, policy_engine_mode):
        """Sets the policy_engine_mode of this FlowSet.


        :param policy_engine_mode: The policy_engine_mode of this FlowSet.
        :type policy_engine_mode: PolicyEngineMode
        """

        self._policy_engine_mode = policy_engine_mode

    @property
    def compatibility_mode(self):
        """Gets the compatibility_mode of this FlowSet.

        Enable compatibility mode, increases compatibility with password managers on mobile devices.

        :return: The compatibility_mode of this FlowSet.
        :rtype: bool
        """
        return self._compatibility_mode

    @compatibility_mode.setter
    def compatibility_mode(self, compatibility_mode):
        """Sets the compatibility_mode of this FlowSet.

        Enable compatibility mode, increases compatibility with password managers on mobile devices.

        :param compatibility_mode: The compatibility_mode of this FlowSet.
        :type compatibility_mode: bool
        """

        self._compatibility_mode = compatibility_mode

    @property
    def export_url(self):
        """Gets the export_url of this FlowSet.

        Get export URL for flow

        :return: The export_url of this FlowSet.
        :rtype: str
        """
        return self._export_url

    @export_url.setter
    def export_url(self, export_url):
        """Sets the export_url of this FlowSet.

        Get export URL for flow

        :param export_url: The export_url of this FlowSet.
        :type export_url: str
        """
        if export_url is None:
            raise ValueError("Invalid value for `export_url`, must not be `None`")

        self._export_url = export_url

    @property
    def layout(self):
        """Gets the layout of this FlowSet.


        :return: The layout of this FlowSet.
        :rtype: FlowLayoutEnum
        """
        return self._layout

    @layout.setter
    def layout(self, layout):
        """Sets the layout of this FlowSet.


        :param layout: The layout of this FlowSet.
        :type layout: FlowLayoutEnum
        """

        self._layout = layout

    @property
    def denied_action(self):
        """Gets the denied_action of this FlowSet.

        Configure what should happen when a flow denies access to a user.

        :return: The denied_action of this FlowSet.
        :rtype: DeniedActionEnum
        """
        return self._denied_action

    @denied_action.setter
    def denied_action(self, denied_action):
        """Sets the denied_action of this FlowSet.

        Configure what should happen when a flow denies access to a user.

        :param denied_action: The denied_action of this FlowSet.
        :type denied_action: DeniedActionEnum
        """

        self._denied_action = denied_action
