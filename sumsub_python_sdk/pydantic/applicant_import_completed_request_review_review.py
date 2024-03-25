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


class ApplicantImportCompletedRequestReviewReview(BaseModel):
    # Reason of rejection for end-user
    moderation_comment: typing.Optional[str] = Field(None, alias='moderationComment')

    # internal reason of rejection
    client_comment: typing.Optional[str] = Field(None, alias='clientComment')

    # \"GREEN\"/\"RED\"
    review_answer: typing.Optional[str] = Field(None, alias='reviewAnswer')

    # \"FINAL\"/\"RETRY\"(used only when \"reviewAnswer\"=\"RED\")
    review_reject_type: typing.Optional[str] = Field(None, alias='reviewRejectType')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
