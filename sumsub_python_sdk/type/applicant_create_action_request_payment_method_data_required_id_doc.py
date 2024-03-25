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


class RequiredApplicantCreateActionRequestPaymentMethodDataRequiredIdDoc(TypedDict):
    pass

class OptionalApplicantCreateActionRequestPaymentMethodDataRequiredIdDoc(TypedDict, total=False):
    firstName: str

    lastName: str

    middleName: str

    number: str

    issuedDate: str

    txnAmount: str

class ApplicantCreateActionRequestPaymentMethodDataRequiredIdDoc(RequiredApplicantCreateActionRequestPaymentMethodDataRequiredIdDoc, OptionalApplicantCreateActionRequestPaymentMethodDataRequiredIdDoc):
    pass
