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


class RequiredAnalysisStandaloneCryptoInitiationRequest(TypedDict):
    # `BTC`, `ETH`, `BCH`, `LTC`, `USDT`, `ERC-20`, `BSV`, `XLM`, ...
    currency: str

    # An operation type. Can be `withdrawal` or `deposit`.
    direction: str

    # Target address hash.
    address: str

class OptionalAnalysisStandaloneCryptoInitiationRequest(TypedDict, total=False):
    # Transaction hash. For `withdrawals`, `txn` should not be set at all or set to `null`.
    txn: str

    # Check the [Get available tokens](ref:get-available-tokens) method to get the full list of available currencies and token IDs.
    tokenId: str

class AnalysisStandaloneCryptoInitiationRequest(RequiredAnalysisStandaloneCryptoInitiationRequest, OptionalAnalysisStandaloneCryptoInitiationRequest):
    pass
