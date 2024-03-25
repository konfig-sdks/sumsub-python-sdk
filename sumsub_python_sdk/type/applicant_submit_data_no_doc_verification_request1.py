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

from sumsub_python_sdk.type.applicant_submit_data_no_doc_verification_request1_info import ApplicantSubmitDataNoDocVerificationRequest1Info

class RequiredApplicantSubmitDataNoDocVerificationRequest1(TypedDict):
    info: ApplicantSubmitDataNoDocVerificationRequest1Info

class OptionalApplicantSubmitDataNoDocVerificationRequest1(TypedDict, total=False):
    pass

class ApplicantSubmitDataNoDocVerificationRequest1(RequiredApplicantSubmitDataNoDocVerificationRequest1, OptionalApplicantSubmitDataNoDocVerificationRequest1):
    pass
