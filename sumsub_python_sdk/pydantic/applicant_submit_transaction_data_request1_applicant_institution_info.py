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

from sumsub_python_sdk.pydantic.applicant_submit_transaction_data_request1_applicant_institution_info_address import ApplicantSubmitTransactionDataRequest1ApplicantInstitutionInfoAddress

class ApplicantSubmitTransactionDataRequest1ApplicantInstitutionInfo(BaseModel):
    # Transaction institution code.
    code: typing.Optional[str] = Field(None, alias='code')

    # Transaction institution name.
    name: typing.Optional[str] = Field(None, alias='name')

    address: typing.Optional[ApplicantSubmitTransactionDataRequest1ApplicantInstitutionInfoAddress] = Field(None, alias='address')

    # VASP ID for counterparty transaction. If provided, we trust the exchange and use the expected VASP for transaction approval.
    internal_id: typing.Optional[str] = Field(None, alias='internalId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
