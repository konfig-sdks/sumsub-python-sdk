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


class ApplicantSubmitTransactionForNonExistingRequest1ApplicantDeviceIpInfo(BaseModel):
    # Position latitude in decimal degrees.
    lat: typing.Optional[typing.Union[int, float]] = Field(None, alias='lat')

    # Position longitude in decimal degrees.
    lon: typing.Optional[typing.Union[int, float]] = Field(None, alias='lon')

    # IP address.
    ip: typing.Optional[str] = Field(None, alias='ip')

    # Country Alpha-3 code.
    country_code3: typing.Optional[str] = Field(None, alias='countryCode3')

    # ASN.
    asn: typing.Optional[int] = Field(None, alias='asn')

    # ASN organisation.
    asn_org: typing.Optional[str] = Field(None, alias='asnOrg')

    # ASN is risky or not.
    risky_asn: typing.Optional[bool] = Field(None, alias='riskyAsn')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
