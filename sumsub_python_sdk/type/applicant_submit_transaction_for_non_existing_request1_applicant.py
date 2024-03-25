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

from sumsub_python_sdk.type.applicant_submit_transaction_for_non_existing_request1_applicant_address import ApplicantSubmitTransactionForNonExistingRequest1ApplicantAddress
from sumsub_python_sdk.type.applicant_submit_transaction_for_non_existing_request1_applicant_device import ApplicantSubmitTransactionForNonExistingRequest1ApplicantDevice
from sumsub_python_sdk.type.applicant_submit_transaction_for_non_existing_request1_applicant_id_docs import ApplicantSubmitTransactionForNonExistingRequest1ApplicantIdDocs
from sumsub_python_sdk.type.applicant_submit_transaction_for_non_existing_request1_applicant_institution_info import ApplicantSubmitTransactionForNonExistingRequest1ApplicantInstitutionInfo
from sumsub_python_sdk.type.applicant_submit_transaction_for_non_existing_request1_applicant_payment_method import ApplicantSubmitTransactionForNonExistingRequest1ApplicantPaymentMethod

class RequiredApplicantSubmitTransactionForNonExistingRequest1Applicant(TypedDict):
    # An external identifier of the transaction participant (applicant or counterparty). Each participant must have a unique identifier that must be reused during all subsequent transactions. Make sure to use the same `externalUserID` for the same counterparty or applicant.
    externalUserId: str

    # Full name of the participant.
    fullName: str

    # Participant entity type: `company` or `individual`. Set to `individual` by default.
    type: str

class OptionalApplicantSubmitTransactionForNonExistingRequest1Applicant(TypedDict, total=False):
    address: ApplicantSubmitTransactionForNonExistingRequest1ApplicantAddress

    institutionInfo: ApplicantSubmitTransactionForNonExistingRequest1ApplicantInstitutionInfo

    paymentMethod: ApplicantSubmitTransactionForNonExistingRequest1ApplicantPaymentMethod

    device: ApplicantSubmitTransactionForNonExistingRequest1ApplicantDevice

    idDocs: ApplicantSubmitTransactionForNonExistingRequest1ApplicantIdDocs

class ApplicantSubmitTransactionForNonExistingRequest1Applicant(RequiredApplicantSubmitTransactionForNonExistingRequest1Applicant, OptionalApplicantSubmitTransactionForNonExistingRequest1Applicant):
    pass
