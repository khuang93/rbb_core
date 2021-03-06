# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from rbb_swagger_server.models.base_model_ import Model
from rbb_swagger_server.models.file_summary import FileSummary  # noqa: F401,E501
from rbb_swagger_server import util


class ProductFile(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, key: str=None, file: FileSummary=None):  # noqa: E501
        """ProductFile - a model defined in Swagger

        :param key: The key of this ProductFile.  # noqa: E501
        :type key: str
        :param file: The file of this ProductFile.  # noqa: E501
        :type file: FileSummary
        """
        self.swagger_types = {
            'key': str,
            'file': FileSummary
        }

        self.attribute_map = {
            'key': 'key',
            'file': 'file'
        }

        self._key = key
        self._file = file

    @classmethod
    def from_dict(cls, dikt) -> 'ProductFile':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ProductFile of this ProductFile.  # noqa: E501
        :rtype: ProductFile
        """
        return util.deserialize_model(dikt, cls)

    @property
    def key(self) -> str:
        """Gets the key of this ProductFile.

        Key that links the file to the product  # noqa: E501

        :return: The key of this ProductFile.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key: str):
        """Sets the key of this ProductFile.

        Key that links the file to the product  # noqa: E501

        :param key: The key of this ProductFile.
        :type key: str
        """

        self._key = key

    @property
    def file(self) -> FileSummary:
        """Gets the file of this ProductFile.


        :return: The file of this ProductFile.
        :rtype: FileSummary
        """
        return self._file

    @file.setter
    def file(self, file: FileSummary):
        """Sets the file of this ProductFile.


        :param file: The file of this ProductFile.
        :type file: FileSummary
        """

        self._file = file
