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

from sumsub_python_sdk.type.applicant_submit_transaction_data_request1_counterparty_institution_info_address import ApplicantSubmitTransactionDataRequest1CounterpartyInstitutionInfoAddress

class RequiredApplicantSubmitTransactionDataRequest1CounterpartyInstitutionInfo(TypedDict):
    pass

class OptionalApplicantSubmitTransactionDataRequest1CounterpartyInstitutionInfo(TypedDict, total=False):
    # Transaction institution code.
    code: str

    # Transaction institution name.
    name: str

    address: ApplicantSubmitTransactionDataRequest1CounterpartyInstitutionInfoAddress

    # VASP ID for counterparty transaction. If provided, we trust the exchange and use the expected VASP for transaction approval.
    internalId: str

class ApplicantSubmitTransactionDataRequest1CounterpartyInstitutionInfo(RequiredApplicantSubmitTransactionDataRequest1CounterpartyInstitutionInfo, OptionalApplicantSubmitTransactionDataRequest1CounterpartyInstitutionInfo):
    pass
