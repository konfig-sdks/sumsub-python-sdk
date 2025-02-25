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


class ApplicantCreatePaymentSourceActionsResponseReview(BaseModel):
    review_id: typing.Optional[str] = Field(None, alias='reviewId')

    attempt_id: typing.Optional[str] = Field(None, alias='attemptId')

    attempt_cnt: typing.Optional[int] = Field(None, alias='attemptCnt')

    level_name: typing.Optional[str] = Field(None, alias='levelName')

    create_date: typing.Optional[str] = Field(None, alias='createDate')

    review_status: typing.Optional[str] = Field(None, alias='reviewStatus')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
