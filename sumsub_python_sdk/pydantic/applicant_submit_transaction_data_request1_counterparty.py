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

from sumsub_python_sdk.pydantic.applicant_submit_transaction_data_request1_counterparty_address import ApplicantSubmitTransactionDataRequest1CounterpartyAddress
from sumsub_python_sdk.pydantic.applicant_submit_transaction_data_request1_counterparty_device import ApplicantSubmitTransactionDataRequest1CounterpartyDevice
from sumsub_python_sdk.pydantic.applicant_submit_transaction_data_request1_counterparty_id_docs import ApplicantSubmitTransactionDataRequest1CounterpartyIdDocs
from sumsub_python_sdk.pydantic.applicant_submit_transaction_data_request1_counterparty_institution_info import ApplicantSubmitTransactionDataRequest1CounterpartyInstitutionInfo
from sumsub_python_sdk.pydantic.applicant_submit_transaction_data_request1_counterparty_payment_method import ApplicantSubmitTransactionDataRequest1CounterpartyPaymentMethod

class ApplicantSubmitTransactionDataRequest1Counterparty(BaseModel):
    # An external identifier of the transaction participant (applicant or counterparty). Each participant must have a unique identifier that must be reused during all subsequent transactions. Make sure to use the same `externalUserID` for the same counterparty or applicant.
    external_user_id: str = Field(alias='externalUserId')

    # Full name of the participant.
    full_name: str = Field(alias='fullName')

    # Participant entity type: `company` or `individual`. Set to `individual` by default.
    type: str = Field(alias='type')

    address: typing.Optional[ApplicantSubmitTransactionDataRequest1CounterpartyAddress] = Field(None, alias='address')

    institution_info: typing.Optional[ApplicantSubmitTransactionDataRequest1CounterpartyInstitutionInfo] = Field(None, alias='institutionInfo')

    payment_method: typing.Optional[ApplicantSubmitTransactionDataRequest1CounterpartyPaymentMethod] = Field(None, alias='paymentMethod')

    device: typing.Optional[ApplicantSubmitTransactionDataRequest1CounterpartyDevice] = Field(None, alias='device')

    id_docs: typing.Optional[ApplicantSubmitTransactionDataRequest1CounterpartyIdDocs] = Field(None, alias='idDocs')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
