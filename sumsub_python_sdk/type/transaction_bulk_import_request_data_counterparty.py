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

from sumsub_python_sdk.type.transaction_bulk_import_request_data_counterparty_address import TransactionBulkImportRequestDataCounterpartyAddress
from sumsub_python_sdk.type.transaction_bulk_import_request_data_counterparty_device import TransactionBulkImportRequestDataCounterpartyDevice
from sumsub_python_sdk.type.transaction_bulk_import_request_data_counterparty_id_docs import TransactionBulkImportRequestDataCounterpartyIdDocs
from sumsub_python_sdk.type.transaction_bulk_import_request_data_counterparty_institution_info import TransactionBulkImportRequestDataCounterpartyInstitutionInfo
from sumsub_python_sdk.type.transaction_bulk_import_request_data_counterparty_payment_method import TransactionBulkImportRequestDataCounterpartyPaymentMethod

class RequiredTransactionBulkImportRequestDataCounterparty(TypedDict):
    # An external identifier of the transaction participant (applicant or counterparty). Each participant must have a unique identifier that must be reused during all subsequent transactions. Make sure to use the same `externalUserID` for the same counterparty or applicant.
    externalUserId: str

    # Full name of the participant.
    fullName: str

    # Participant entity type: `company` or `individual`. Set to `individual` by default.
    type: str

class OptionalTransactionBulkImportRequestDataCounterparty(TypedDict, total=False):
    address: TransactionBulkImportRequestDataCounterpartyAddress

    institutionInfo: TransactionBulkImportRequestDataCounterpartyInstitutionInfo

    paymentMethod: TransactionBulkImportRequestDataCounterpartyPaymentMethod

    device: TransactionBulkImportRequestDataCounterpartyDevice

    idDocs: TransactionBulkImportRequestDataCounterpartyIdDocs

class TransactionBulkImportRequestDataCounterparty(RequiredTransactionBulkImportRequestDataCounterparty, OptionalTransactionBulkImportRequestDataCounterparty):
    pass
