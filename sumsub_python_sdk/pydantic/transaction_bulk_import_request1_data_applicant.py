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

from sumsub_python_sdk.pydantic.transaction_bulk_import_request1_data_applicant_address import TransactionBulkImportRequest1DataApplicantAddress
from sumsub_python_sdk.pydantic.transaction_bulk_import_request1_data_applicant_device import TransactionBulkImportRequest1DataApplicantDevice
from sumsub_python_sdk.pydantic.transaction_bulk_import_request1_data_applicant_id_docs import TransactionBulkImportRequest1DataApplicantIdDocs
from sumsub_python_sdk.pydantic.transaction_bulk_import_request1_data_applicant_institution_info import TransactionBulkImportRequest1DataApplicantInstitutionInfo
from sumsub_python_sdk.pydantic.transaction_bulk_import_request1_data_applicant_payment_method import TransactionBulkImportRequest1DataApplicantPaymentMethod

class TransactionBulkImportRequest1DataApplicant(BaseModel):
    # An external identifier of the transaction participant (applicant or counterparty). Each participant must have a unique identifier that must be reused during all subsequent transactions. Make sure to use the same `externalUserID` for the same counterparty or applicant.
    external_user_id: str = Field(alias='externalUserId')

    # Full name of the participant.
    full_name: str = Field(alias='fullName')

    # Participant entity type: `company` or `individual`. Set to `individual` by default.
    type: str = Field(alias='type')

    address: typing.Optional[TransactionBulkImportRequest1DataApplicantAddress] = Field(None, alias='address')

    institution_info: typing.Optional[TransactionBulkImportRequest1DataApplicantInstitutionInfo] = Field(None, alias='institutionInfo')

    payment_method: typing.Optional[TransactionBulkImportRequest1DataApplicantPaymentMethod] = Field(None, alias='paymentMethod')

    device: typing.Optional[TransactionBulkImportRequest1DataApplicantDevice] = Field(None, alias='device')

    id_docs: typing.Optional[TransactionBulkImportRequest1DataApplicantIdDocs] = Field(None, alias='idDocs')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
