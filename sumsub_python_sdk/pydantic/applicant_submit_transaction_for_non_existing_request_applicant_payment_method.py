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


class ApplicantSubmitTransactionForNonExistingRequestApplicantPaymentMethod(BaseModel):
    # Payment method type: `card`/`account`/`crypto`.
    type: typing.Optional[str] = Field(None, alias='type')

    # Representation of the account ID: Account number, IBAN or DC hash for `card`, crypto wallet address for `crypto` type etc.
    account_id: typing.Optional[str] = Field(None, alias='accountId')

    # The payment issuing country code in Alpha-3 format.
    issuing_country: typing.Optional[str] = Field(None, alias='issuingCountry')

    # Indication of 3d secure auth being used.
    3ds_used_: typing.Optional[bool] = Field(None, alias='3dsUsed')

    # Indication of 2fa being used.
    2fa_used_: typing.Optional[bool] = Field(None, alias='2faUsed')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
