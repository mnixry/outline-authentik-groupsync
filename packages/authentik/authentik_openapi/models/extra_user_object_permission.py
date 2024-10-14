# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi import util


class ExtraUserObjectPermission(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, codename: str=None, model: str=None, app_label: str=None, object_pk: str=None, name: str=None, app_label_verbose: str=None, model_verbose: str=None, object_description: str=None):
        """ExtraUserObjectPermission - a model defined in OpenAPI

        :param id: The id of this ExtraUserObjectPermission.
        :param codename: The codename of this ExtraUserObjectPermission.
        :param model: The model of this ExtraUserObjectPermission.
        :param app_label: The app_label of this ExtraUserObjectPermission.
        :param object_pk: The object_pk of this ExtraUserObjectPermission.
        :param name: The name of this ExtraUserObjectPermission.
        :param app_label_verbose: The app_label_verbose of this ExtraUserObjectPermission.
        :param model_verbose: The model_verbose of this ExtraUserObjectPermission.
        :param object_description: The object_description of this ExtraUserObjectPermission.
        """
        self.openapi_types = {
            'id': int,
            'codename': str,
            'model': str,
            'app_label': str,
            'object_pk': str,
            'name': str,
            'app_label_verbose': str,
            'model_verbose': str,
            'object_description': str
        }

        self.attribute_map = {
            'id': 'id',
            'codename': 'codename',
            'model': 'model',
            'app_label': 'app_label',
            'object_pk': 'object_pk',
            'name': 'name',
            'app_label_verbose': 'app_label_verbose',
            'model_verbose': 'model_verbose',
            'object_description': 'object_description'
        }

        self._id = id
        self._codename = codename
        self._model = model
        self._app_label = app_label
        self._object_pk = object_pk
        self._name = name
        self._app_label_verbose = app_label_verbose
        self._model_verbose = model_verbose
        self._object_description = object_description

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ExtraUserObjectPermission':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ExtraUserObjectPermission of this ExtraUserObjectPermission.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this ExtraUserObjectPermission.


        :return: The id of this ExtraUserObjectPermission.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExtraUserObjectPermission.


        :param id: The id of this ExtraUserObjectPermission.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def codename(self):
        """Gets the codename of this ExtraUserObjectPermission.


        :return: The codename of this ExtraUserObjectPermission.
        :rtype: str
        """
        return self._codename

    @codename.setter
    def codename(self, codename):
        """Sets the codename of this ExtraUserObjectPermission.


        :param codename: The codename of this ExtraUserObjectPermission.
        :type codename: str
        """
        if codename is None:
            raise ValueError("Invalid value for `codename`, must not be `None`")

        self._codename = codename

    @property
    def model(self):
        """Gets the model of this ExtraUserObjectPermission.


        :return: The model of this ExtraUserObjectPermission.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this ExtraUserObjectPermission.


        :param model: The model of this ExtraUserObjectPermission.
        :type model: str
        """
        if model is None:
            raise ValueError("Invalid value for `model`, must not be `None`")

        self._model = model

    @property
    def app_label(self):
        """Gets the app_label of this ExtraUserObjectPermission.


        :return: The app_label of this ExtraUserObjectPermission.
        :rtype: str
        """
        return self._app_label

    @app_label.setter
    def app_label(self, app_label):
        """Sets the app_label of this ExtraUserObjectPermission.


        :param app_label: The app_label of this ExtraUserObjectPermission.
        :type app_label: str
        """
        if app_label is None:
            raise ValueError("Invalid value for `app_label`, must not be `None`")

        self._app_label = app_label

    @property
    def object_pk(self):
        """Gets the object_pk of this ExtraUserObjectPermission.


        :return: The object_pk of this ExtraUserObjectPermission.
        :rtype: str
        """
        return self._object_pk

    @object_pk.setter
    def object_pk(self, object_pk):
        """Sets the object_pk of this ExtraUserObjectPermission.


        :param object_pk: The object_pk of this ExtraUserObjectPermission.
        :type object_pk: str
        """
        if object_pk is None:
            raise ValueError("Invalid value for `object_pk`, must not be `None`")

        self._object_pk = object_pk

    @property
    def name(self):
        """Gets the name of this ExtraUserObjectPermission.


        :return: The name of this ExtraUserObjectPermission.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ExtraUserObjectPermission.


        :param name: The name of this ExtraUserObjectPermission.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def app_label_verbose(self):
        """Gets the app_label_verbose of this ExtraUserObjectPermission.

        Get app label from permission's model

        :return: The app_label_verbose of this ExtraUserObjectPermission.
        :rtype: str
        """
        return self._app_label_verbose

    @app_label_verbose.setter
    def app_label_verbose(self, app_label_verbose):
        """Sets the app_label_verbose of this ExtraUserObjectPermission.

        Get app label from permission's model

        :param app_label_verbose: The app_label_verbose of this ExtraUserObjectPermission.
        :type app_label_verbose: str
        """
        if app_label_verbose is None:
            raise ValueError("Invalid value for `app_label_verbose`, must not be `None`")

        self._app_label_verbose = app_label_verbose

    @property
    def model_verbose(self):
        """Gets the model_verbose of this ExtraUserObjectPermission.

        Get model label from permission's model

        :return: The model_verbose of this ExtraUserObjectPermission.
        :rtype: str
        """
        return self._model_verbose

    @model_verbose.setter
    def model_verbose(self, model_verbose):
        """Sets the model_verbose of this ExtraUserObjectPermission.

        Get model label from permission's model

        :param model_verbose: The model_verbose of this ExtraUserObjectPermission.
        :type model_verbose: str
        """
        if model_verbose is None:
            raise ValueError("Invalid value for `model_verbose`, must not be `None`")

        self._model_verbose = model_verbose

    @property
    def object_description(self):
        """Gets the object_description of this ExtraUserObjectPermission.

        Get model description from attached model. This operation takes at least one additional query, and the description is only shown if the user/role has the view_ permission on the object

        :return: The object_description of this ExtraUserObjectPermission.
        :rtype: str
        """
        return self._object_description

    @object_description.setter
    def object_description(self, object_description):
        """Sets the object_description of this ExtraUserObjectPermission.

        Get model description from attached model. This operation takes at least one additional query, and the description is only shown if the user/role has the view_ permission on the object

        :param object_description: The object_description of this ExtraUserObjectPermission.
        :type object_description: str
        """
        if object_description is None:
            raise ValueError("Invalid value for `object_description`, must not be `None`")

        self._object_description = object_description
