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


class TransactionBulkImportRequestDataApplicantPaymentMethod(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Information about the payment method.
    """


    class MetaOapg:
        
        class properties:
            type = schemas.StrSchema
            accountId = schemas.StrSchema
            issuingCountry = schemas.StrSchema
            _3ds_used = schemas.BoolSchema
            _2fa_used = schemas.BoolSchema
            __annotations__ = {
                "type": type,
                "accountId": accountId,
                "issuingCountry": issuingCountry,
                "3dsUsed": _3ds_used,
                "2faUsed": _2fa_used,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountId"]) -> MetaOapg.properties.accountId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["issuingCountry"]) -> MetaOapg.properties.issuingCountry: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["3dsUsed"]) -> MetaOapg.properties._3ds_used: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["2faUsed"]) -> MetaOapg.properties._2fa_used: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "accountId", "issuingCountry", "3dsUsed", "2faUsed", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountId"]) -> typing.Union[MetaOapg.properties.accountId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["issuingCountry"]) -> typing.Union[MetaOapg.properties.issuingCountry, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["3dsUsed"]) -> typing.Union[MetaOapg.properties._3ds_used, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["2faUsed"]) -> typing.Union[MetaOapg.properties._2fa_used, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "accountId", "issuingCountry", "3dsUsed", "2faUsed", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        accountId: typing.Union[MetaOapg.properties.accountId, str, schemas.Unset] = schemas.unset,
        issuingCountry: typing.Union[MetaOapg.properties.issuingCountry, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TransactionBulkImportRequestDataApplicantPaymentMethod':
        return super().__new__(
            cls,
            *args,
            type=type,
            accountId=accountId,
            issuingCountry=issuingCountry,
            _configuration=_configuration,
            **kwargs,
        )
