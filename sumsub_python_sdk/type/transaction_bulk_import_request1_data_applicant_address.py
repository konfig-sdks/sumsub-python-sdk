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


class RequiredTransactionBulkImportRequest1DataApplicantAddress(TypedDict):
    pass

class OptionalTransactionBulkImportRequest1DataApplicantAddress(TypedDict, total=False):
    # Alpha-3 country code.
    country: str

    # Postal code.
    postCode: str

    # Town or city name.
    town: str

    # Street name.
    street: str

    # Additional street information.
    subStreet: str

    # State name (if applicable).
    state: str

    # Building name (if applicable).
    buildingName: str

    # Flat or apartment number.
    flatNumber: str

    # Building number.
    buildingNumber: str

class TransactionBulkImportRequest1DataApplicantAddress(RequiredTransactionBulkImportRequest1DataApplicantAddress, OptionalTransactionBulkImportRequest1DataApplicantAddress):
    pass
