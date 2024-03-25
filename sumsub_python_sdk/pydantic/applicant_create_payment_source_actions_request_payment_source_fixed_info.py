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


class ApplicantCreatePaymentSourceActionsRequestPaymentSourceFixedInfo(BaseModel):
    # A unique identifier for an account (e.g., \"123456\").
    account_identifier: typing.Optional[str] = Field(None, alias='accountIdentifier')

    # An email address associated with a particular account.
    email: typing.Optional[str] = Field(None, alias='email')

    # The full name of an account holder (e.g., \"Alex Kim\").
    full_name: typing.Optional[str] = Field(None, alias='fullName')

    # A name of the financial institution where an account is held (e.g., Revolut).
    institution_name: typing.Optional[str] = Field(None, alias='institutionName')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
