# coding: utf-8

"""
    Sumsub API

    Sumsub is the one verification platform to secure the whole user journey. With Sumsub's customizable KYC, KYB, transaction monitoring and fraud prevention solutions, you can orchestrate your verification process, welcome more customers worldwide, meet compliance requirements, reduce costs and protect your business.  Sumsub has over 2,000 clients in fintech, crypto, transportation, trading, e-commerce and gaming industries including Binance, Wirex, Avis, Bybit, Huobi, Unlimit, Flutter, Kaizen Gaming, and TransferGo.

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from sumsub_python_sdk import schemas  # noqa: F401


class ApplicantSubmitTransactionForNonExistingRequestCounterpartyIdDocs(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    Data about the user and their documents.
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['ApplicantSubmitTransactionForNonExistingRequestCounterpartyIdDocsItem']:
            return ApplicantSubmitTransactionForNonExistingRequestCounterpartyIdDocsItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['ApplicantSubmitTransactionForNonExistingRequestCounterpartyIdDocsItem'], typing.List['ApplicantSubmitTransactionForNonExistingRequestCounterpartyIdDocsItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ApplicantSubmitTransactionForNonExistingRequestCounterpartyIdDocs':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'ApplicantSubmitTransactionForNonExistingRequestCounterpartyIdDocsItem':
        return super().__getitem__(i)

from sumsub_python_sdk.model.applicant_submit_transaction_for_non_existing_request_counterparty_id_docs_item import ApplicantSubmitTransactionForNonExistingRequestCounterpartyIdDocsItem
