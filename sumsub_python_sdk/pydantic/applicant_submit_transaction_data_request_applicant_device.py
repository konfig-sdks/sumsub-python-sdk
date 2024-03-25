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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from sumsub_python_sdk.pydantic.applicant_submit_transaction_data_request_applicant_device_address import ApplicantSubmitTransactionDataRequestApplicantDeviceAddress
from sumsub_python_sdk.pydantic.applicant_submit_transaction_data_request_applicant_device_coords import ApplicantSubmitTransactionDataRequestApplicantDeviceCoords
from sumsub_python_sdk.pydantic.applicant_submit_transaction_data_request_applicant_device_ip_info import ApplicantSubmitTransactionDataRequestApplicantDeviceIpInfo

class ApplicantSubmitTransactionDataRequestApplicantDevice(BaseModel):
    # Device user agent.
    user_agent: typing.Optional[str] = Field(None, alias='userAgent')

    # Transaction session identifier.
    session_id: typing.Optional[str] = Field(None, alias='sessionId')

    # Session lifetime in milliseconds.
    session_age_ms: typing.Optional[int] = Field(None, alias='sessionAgeMs')

    # From browser, e.g. `en`.
    accept_lang: typing.Optional[str] = Field(None, alias='acceptLang')

    # Device platform, e.g. `Mobile Android`.
    platform: typing.Optional[str] = Field(None, alias='platform')

    # Device fingerprint.
    fingerprint: typing.Optional[str] = Field(None, alias='fingerprint')

    address: typing.Optional[ApplicantSubmitTransactionDataRequestApplicantDeviceAddress] = Field(None, alias='address')

    coords: typing.Optional[ApplicantSubmitTransactionDataRequestApplicantDeviceCoords] = Field(None, alias='coords')

    ip_info: typing.Optional[ApplicantSubmitTransactionDataRequestApplicantDeviceIpInfo] = Field(None, alias='ipInfo')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
