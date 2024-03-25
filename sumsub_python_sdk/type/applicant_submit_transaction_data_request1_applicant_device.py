# coding: utf-8

"""
    Sumsub API

    Sumsub is the one verification platform to secure the whole user journey. With Sumsub's customizable KYC, KYB, transaction monitoring and fraud prevention solutions, you can orchestrate your verification process, welcome more customers worldwide, meet compliance requirements, reduce costs and protect your business.  Sumsub has over 2,000 clients in fintech, crypto, transportation, trading, e-commerce and gaming industries including Binance, Wirex, Avis, Bybit, Huobi, Unlimit, Flutter, Kaizen Gaming, and TransferGo.

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from sumsub_python_sdk.type.applicant_submit_transaction_data_request1_applicant_device_address import ApplicantSubmitTransactionDataRequest1ApplicantDeviceAddress
from sumsub_python_sdk.type.applicant_submit_transaction_data_request1_applicant_device_coords import ApplicantSubmitTransactionDataRequest1ApplicantDeviceCoords
from sumsub_python_sdk.type.applicant_submit_transaction_data_request1_applicant_device_ip_info import ApplicantSubmitTransactionDataRequest1ApplicantDeviceIpInfo

class RequiredApplicantSubmitTransactionDataRequest1ApplicantDevice(TypedDict):
    pass

class OptionalApplicantSubmitTransactionDataRequest1ApplicantDevice(TypedDict, total=False):
    # Device user agent.
    userAgent: str

    # Transaction session identifier.
    sessionId: str

    # Session lifetime in milliseconds.
    sessionAgeMs: int

    # From browser, e.g. `en`.
    acceptLang: str

    # Device platform, e.g. `Mobile Android`.
    platform: str

    # Device fingerprint.
    fingerprint: str

    address: ApplicantSubmitTransactionDataRequest1ApplicantDeviceAddress

    coords: ApplicantSubmitTransactionDataRequest1ApplicantDeviceCoords

    ipInfo: ApplicantSubmitTransactionDataRequest1ApplicantDeviceIpInfo

class ApplicantSubmitTransactionDataRequest1ApplicantDevice(RequiredApplicantSubmitTransactionDataRequest1ApplicantDevice, OptionalApplicantSubmitTransactionDataRequest1ApplicantDevice):
    pass
