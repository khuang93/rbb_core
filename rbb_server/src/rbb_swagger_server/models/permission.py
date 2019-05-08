# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rbb_swagger_server.models.base_model_ import Model
from rbb_swagger_server import util


class Permission(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, identifier: str=None, name: str=None, granted: bool=None):  # noqa: E501
        """Permission - a model defined in Swagger

        :param identifier: The identifier of this Permission.  # noqa: E501
        :type identifier: str
        :param name: The name of this Permission.  # noqa: E501
        :type name: str
        :param granted: The granted of this Permission.  # noqa: E501
        :type granted: bool
        """
        self.swagger_types = {
            'identifier': str,
            'name': str,
            'granted': bool
        }

        self.attribute_map = {
            'identifier': 'identifier',
            'name': 'name',
            'granted': 'granted'
        }

        self._identifier = identifier
        self._name = name
        self._granted = granted

    @classmethod
    def from_dict(cls, dikt) -> 'Permission':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Permission of this Permission.  # noqa: E501
        :rtype: Permission
        """
        return util.deserialize_model(dikt, cls)

    @property
    def identifier(self) -> str:
        """Gets the identifier of this Permission.


        :return: The identifier of this Permission.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier: str):
        """Sets the identifier of this Permission.


        :param identifier: The identifier of this Permission.
        :type identifier: str
        """
        if identifier is None:
            raise ValueError("Invalid value for `identifier`, must not be `None`")  # noqa: E501

        self._identifier = identifier

    @property
    def name(self) -> str:
        """Gets the name of this Permission.


        :return: The name of this Permission.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Permission.


        :param name: The name of this Permission.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def granted(self) -> bool:
        """Gets the granted of this Permission.


        :return: The granted of this Permission.
        :rtype: bool
        """
        return self._granted

    @granted.setter
    def granted(self, granted: bool):
        """Sets the granted of this Permission.


        :param granted: The granted of this Permission.
        :type granted: bool
        """

        self._granted = granted