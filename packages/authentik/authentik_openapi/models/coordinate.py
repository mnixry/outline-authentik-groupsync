# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from authentik_openapi.models.base_model import Model
from authentik_openapi import util


class Coordinate(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, x_cord: int=None, y_cord: int=None):
        """Coordinate - a model defined in OpenAPI

        :param x_cord: The x_cord of this Coordinate.
        :param y_cord: The y_cord of this Coordinate.
        """
        self.openapi_types = {
            'x_cord': int,
            'y_cord': int
        }

        self.attribute_map = {
            'x_cord': 'x_cord',
            'y_cord': 'y_cord'
        }

        self._x_cord = x_cord
        self._y_cord = y_cord

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Coordinate':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Coordinate of this Coordinate.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def x_cord(self):
        """Gets the x_cord of this Coordinate.


        :return: The x_cord of this Coordinate.
        :rtype: int
        """
        return self._x_cord

    @x_cord.setter
    def x_cord(self, x_cord):
        """Sets the x_cord of this Coordinate.


        :param x_cord: The x_cord of this Coordinate.
        :type x_cord: int
        """
        if x_cord is None:
            raise ValueError("Invalid value for `x_cord`, must not be `None`")

        self._x_cord = x_cord

    @property
    def y_cord(self):
        """Gets the y_cord of this Coordinate.


        :return: The y_cord of this Coordinate.
        :rtype: int
        """
        return self._y_cord

    @y_cord.setter
    def y_cord(self, y_cord):
        """Sets the y_cord of this Coordinate.


        :param y_cord: The y_cord of this Coordinate.
        :type y_cord: int
        """
        if y_cord is None:
            raise ValueError("Invalid value for `y_cord`, must not be `None`")

        self._y_cord = y_cord
