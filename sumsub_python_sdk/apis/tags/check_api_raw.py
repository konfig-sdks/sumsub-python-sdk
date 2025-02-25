# coding: utf-8

"""
    Sumsub API

    Sumsub is the one verification platform to secure the whole user journey. With Sumsub's customizable KYC, KYB, transaction monitoring and fraud prevention solutions, you can orchestrate your verification process, welcome more customers worldwide, meet compliance requirements, reduce costs and protect your business.  Sumsub has over 2,000 clients in fintech, crypto, transportation, trading, e-commerce and gaming industries including Binance, Wirex, Avis, Bybit, Huobi, Unlimit, Flutter, Kaizen Gaming, and TransferGo.

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from sumsub_python_sdk.paths.resources_checks_latesttype_company.get import AdditionalCompanyDataRaw
from sumsub_python_sdk.paths.resources_checks_latesttype_poa.get import AdditionalPoaDataRaw
from sumsub_python_sdk.paths.resources_checks_latesttype_email_confirmation.get import EmailConfirmationResultsRaw
from sumsub_python_sdk.paths.resources_checks_latesttype_ip_check.get import IpCheckResultsRaw
from sumsub_python_sdk.paths.resources_checks_cross_checkcomparison_modecomparison_mode.post import PerformNameCrossValidationRaw
from sumsub_python_sdk.paths.resources_checks_latesttype_phone_confirmation.get import PhoneConfirmationResultsRaw
from sumsub_python_sdk.paths.resources_checks_latesttype_tin.get import TinSsnCheckResultsRaw


class CheckApiRaw(
    AdditionalCompanyDataRaw,
    AdditionalPoaDataRaw,
    EmailConfirmationResultsRaw,
    IpCheckResultsRaw,
    PerformNameCrossValidationRaw,
    PhoneConfirmationResultsRaw,
    TinSsnCheckResultsRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
