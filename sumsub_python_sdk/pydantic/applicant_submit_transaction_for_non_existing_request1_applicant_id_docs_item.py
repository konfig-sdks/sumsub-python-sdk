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


class ApplicantSubmitTransactionForNonExistingRequest1ApplicantIdDocsItem(BaseModel):
    # A [document type](ref:add-id-documents#supported-document-types).
    id_doc_type: typing.Optional[str] = Field(None, alias='idDocType')

    # Date of birth (format YYYY-mm-dd, e.g. 2001-09-25).
    dob: typing.Optional[str] = Field(None, alias='dob')

    # Birthplace.
    place_of_birth: typing.Optional[str] = Field(None, alias='placeOfBirth')

    # Alpha-3 country code of the provided document.
    country: typing.Optional[str] = Field(None, alias='country')

    # A document number.
    number: typing.Optional[str] = Field(None, alias='number')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
