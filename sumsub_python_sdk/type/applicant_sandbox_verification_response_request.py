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

from sumsub_python_sdk.type.applicant_sandbox_verification_response_request_reject_labels import ApplicantSandboxVerificationResponseRequestRejectLabels

class RequiredApplicantSandboxVerificationResponseRequest(TypedDict):
    # A `GREEN` or `RED` label under which you want to simulate the response. For more information, see [this article](https://docs.sumsub.com/reference).
    reviewAnswer: str

    rejectLabels: ApplicantSandboxVerificationResponseRequestRejectLabels

class OptionalApplicantSandboxVerificationResponseRequest(TypedDict, total=False):
    # A `FINAL` or `RETRY` rejection type indicating whether a rejection should be final or temporary.
    reviewRejectType: str

    # A rejection comment that should not be available to your applicants.
    clientComment: str

    # A comment that supposed to be shown to the applicant, explaining the reason of rejection.
    moderationComment: str

class ApplicantSandboxVerificationResponseRequest(RequiredApplicantSandboxVerificationResponseRequest, OptionalApplicantSandboxVerificationResponseRequest):
    pass
