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


class TransactionBulkImportRequest1DataApplicant(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Transaction participant data with mandatory `applicantId` (sender or remitter depending on `info.direction`).
    """


    class MetaOapg:
        required = {
            "externalUserId",
            "fullName",
            "type",
        }
        
        class properties:
            externalUserId = schemas.StrSchema
            fullName = schemas.StrSchema
            type = schemas.StrSchema
        
            @staticmethod
            def address() -> typing.Type['TransactionBulkImportRequest1DataApplicantAddress']:
                return TransactionBulkImportRequest1DataApplicantAddress
        
            @staticmethod
            def institutionInfo() -> typing.Type['TransactionBulkImportRequest1DataApplicantInstitutionInfo']:
                return TransactionBulkImportRequest1DataApplicantInstitutionInfo
        
            @staticmethod
            def paymentMethod() -> typing.Type['TransactionBulkImportRequest1DataApplicantPaymentMethod']:
                return TransactionBulkImportRequest1DataApplicantPaymentMethod
        
            @staticmethod
            def device() -> typing.Type['TransactionBulkImportRequest1DataApplicantDevice']:
                return TransactionBulkImportRequest1DataApplicantDevice
        
            @staticmethod
            def idDocs() -> typing.Type['TransactionBulkImportRequest1DataApplicantIdDocs']:
                return TransactionBulkImportRequest1DataApplicantIdDocs
            __annotations__ = {
                "externalUserId": externalUserId,
                "fullName": fullName,
                "type": type,
                "address": address,
                "institutionInfo": institutionInfo,
                "paymentMethod": paymentMethod,
                "device": device,
                "idDocs": idDocs,
            }
    
    externalUserId: MetaOapg.properties.externalUserId
    fullName: MetaOapg.properties.fullName
    type: MetaOapg.properties.type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["externalUserId"]) -> MetaOapg.properties.externalUserId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fullName"]) -> MetaOapg.properties.fullName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address"]) -> 'TransactionBulkImportRequest1DataApplicantAddress': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["institutionInfo"]) -> 'TransactionBulkImportRequest1DataApplicantInstitutionInfo': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paymentMethod"]) -> 'TransactionBulkImportRequest1DataApplicantPaymentMethod': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["device"]) -> 'TransactionBulkImportRequest1DataApplicantDevice': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["idDocs"]) -> 'TransactionBulkImportRequest1DataApplicantIdDocs': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["externalUserId", "fullName", "type", "address", "institutionInfo", "paymentMethod", "device", "idDocs", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["externalUserId"]) -> MetaOapg.properties.externalUserId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fullName"]) -> MetaOapg.properties.fullName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> typing.Union['TransactionBulkImportRequest1DataApplicantAddress', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["institutionInfo"]) -> typing.Union['TransactionBulkImportRequest1DataApplicantInstitutionInfo', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paymentMethod"]) -> typing.Union['TransactionBulkImportRequest1DataApplicantPaymentMethod', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["device"]) -> typing.Union['TransactionBulkImportRequest1DataApplicantDevice', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["idDocs"]) -> typing.Union['TransactionBulkImportRequest1DataApplicantIdDocs', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["externalUserId", "fullName", "type", "address", "institutionInfo", "paymentMethod", "device", "idDocs", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        externalUserId: typing.Union[MetaOapg.properties.externalUserId, str, ],
        fullName: typing.Union[MetaOapg.properties.fullName, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        address: typing.Union['TransactionBulkImportRequest1DataApplicantAddress', schemas.Unset] = schemas.unset,
        institutionInfo: typing.Union['TransactionBulkImportRequest1DataApplicantInstitutionInfo', schemas.Unset] = schemas.unset,
        paymentMethod: typing.Union['TransactionBulkImportRequest1DataApplicantPaymentMethod', schemas.Unset] = schemas.unset,
        device: typing.Union['TransactionBulkImportRequest1DataApplicantDevice', schemas.Unset] = schemas.unset,
        idDocs: typing.Union['TransactionBulkImportRequest1DataApplicantIdDocs', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TransactionBulkImportRequest1DataApplicant':
        return super().__new__(
            cls,
            *args,
            externalUserId=externalUserId,
            fullName=fullName,
            type=type,
            address=address,
            institutionInfo=institutionInfo,
            paymentMethod=paymentMethod,
            device=device,
            idDocs=idDocs,
            _configuration=_configuration,
            **kwargs,
        )

from sumsub_python_sdk.model.transaction_bulk_import_request1_data_applicant_address import TransactionBulkImportRequest1DataApplicantAddress
from sumsub_python_sdk.model.transaction_bulk_import_request1_data_applicant_device import TransactionBulkImportRequest1DataApplicantDevice
from sumsub_python_sdk.model.transaction_bulk_import_request1_data_applicant_id_docs import TransactionBulkImportRequest1DataApplicantIdDocs
from sumsub_python_sdk.model.transaction_bulk_import_request1_data_applicant_institution_info import TransactionBulkImportRequest1DataApplicantInstitutionInfo
from sumsub_python_sdk.model.transaction_bulk_import_request1_data_applicant_payment_method import TransactionBulkImportRequest1DataApplicantPaymentMethod
