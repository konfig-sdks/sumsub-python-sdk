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


class ApplicantSubmitTransactionDataRequestInfo(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    An object representing transaction information.
    """


    class MetaOapg:
        required = {
            "amount",
            "currencyCode",
            "direction",
        }
        
        class properties:
            direction = schemas.StrSchema
            amount = schemas.Float64Schema
            currencyCode = schemas.StrSchema
            amountInDefaultCurrency = schemas.Float64Schema
            cryptoChain = schemas.StrSchema
            paymentTxnId = schemas.StrSchema
            paymentDetails = schemas.StrSchema
            type = schemas.StrSchema
            __annotations__ = {
                "direction": direction,
                "amount": amount,
                "currencyCode": currencyCode,
                "amountInDefaultCurrency": amountInDefaultCurrency,
                "cryptoChain": cryptoChain,
                "paymentTxnId": paymentTxnId,
                "paymentDetails": paymentDetails,
                "type": type,
            }
    
    amount: MetaOapg.properties.amount
    currencyCode: MetaOapg.properties.currencyCode
    direction: MetaOapg.properties.direction
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["direction"]) -> MetaOapg.properties.direction: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currencyCode"]) -> MetaOapg.properties.currencyCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amountInDefaultCurrency"]) -> MetaOapg.properties.amountInDefaultCurrency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cryptoChain"]) -> MetaOapg.properties.cryptoChain: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paymentTxnId"]) -> MetaOapg.properties.paymentTxnId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paymentDetails"]) -> MetaOapg.properties.paymentDetails: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["direction", "amount", "currencyCode", "amountInDefaultCurrency", "cryptoChain", "paymentTxnId", "paymentDetails", "type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["direction"]) -> MetaOapg.properties.direction: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currencyCode"]) -> MetaOapg.properties.currencyCode: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amountInDefaultCurrency"]) -> typing.Union[MetaOapg.properties.amountInDefaultCurrency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cryptoChain"]) -> typing.Union[MetaOapg.properties.cryptoChain, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paymentTxnId"]) -> typing.Union[MetaOapg.properties.paymentTxnId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paymentDetails"]) -> typing.Union[MetaOapg.properties.paymentDetails, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["direction", "amount", "currencyCode", "amountInDefaultCurrency", "cryptoChain", "paymentTxnId", "paymentDetails", "type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        amount: typing.Union[MetaOapg.properties.amount, decimal.Decimal, int, float, ],
        currencyCode: typing.Union[MetaOapg.properties.currencyCode, str, ],
        direction: typing.Union[MetaOapg.properties.direction, str, ],
        amountInDefaultCurrency: typing.Union[MetaOapg.properties.amountInDefaultCurrency, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        cryptoChain: typing.Union[MetaOapg.properties.cryptoChain, str, schemas.Unset] = schemas.unset,
        paymentTxnId: typing.Union[MetaOapg.properties.paymentTxnId, str, schemas.Unset] = schemas.unset,
        paymentDetails: typing.Union[MetaOapg.properties.paymentDetails, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ApplicantSubmitTransactionDataRequestInfo':
        return super().__new__(
            cls,
            *args,
            amount=amount,
            currencyCode=currencyCode,
            direction=direction,
            amountInDefaultCurrency=amountInDefaultCurrency,
            cryptoChain=cryptoChain,
            paymentTxnId=paymentTxnId,
            paymentDetails=paymentDetails,
            type=type,
            _configuration=_configuration,
            **kwargs,
        )
