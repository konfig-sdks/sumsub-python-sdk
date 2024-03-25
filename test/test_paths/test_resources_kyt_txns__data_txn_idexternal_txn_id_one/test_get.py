# coding: utf-8

"""
    Sumsub API

    Sumsub is the one verification platform to secure the whole user journey. With Sumsub's customizable KYC, KYB, transaction monitoring and fraud prevention solutions, you can orchestrate your verification process, welcome more customers worldwide, meet compliance requirements, reduce costs and protect your business.  Sumsub has over 2,000 clients in fintech, crypto, transportation, trading, e-commerce and gaming industries including Binance, Wirex, Avis, Bybit, Huobi, Unlimit, Flutter, Kaizen Gaming, and TransferGo.

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import sumsub_python_sdk
from sumsub_python_sdk.paths.resources_kyt_txns__data_txn_idexternal_txn_id_one import get
from sumsub_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestResourcesKytTxnsDataTxnIdexternalTxnIdOne(ApiTestMixin, unittest.TestCase):
    """
    ResourcesKytTxnsDataTxnIdexternalTxnIdOne unit test stubs
        Get transaction information (externalTxnId)
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200
    response_body = ''


if __name__ == '__main__':
    unittest.main()
