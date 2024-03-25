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


class ApplicantAddPaymentMethodInformationRequestDataRequiredIdDoc(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            firstName = schemas.StrSchema
            lastName = schemas.StrSchema
            middleName = schemas.StrSchema
            number = schemas.StrSchema
            issuedDate = schemas.StrSchema
            txnAmount = schemas.StrSchema
            __annotations__ = {
                "firstName": firstName,
                "lastName": lastName,
                "middleName": middleName,
                "number": number,
                "issuedDate": issuedDate,
                "txnAmount": txnAmount,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firstName"]) -> MetaOapg.properties.firstName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastName"]) -> MetaOapg.properties.lastName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["middleName"]) -> MetaOapg.properties.middleName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["number"]) -> MetaOapg.properties.number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["issuedDate"]) -> MetaOapg.properties.issuedDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["txnAmount"]) -> MetaOapg.properties.txnAmount: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["firstName", "lastName", "middleName", "number", "issuedDate", "txnAmount", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firstName"]) -> typing.Union[MetaOapg.properties.firstName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastName"]) -> typing.Union[MetaOapg.properties.lastName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["middleName"]) -> typing.Union[MetaOapg.properties.middleName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["number"]) -> typing.Union[MetaOapg.properties.number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["issuedDate"]) -> typing.Union[MetaOapg.properties.issuedDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["txnAmount"]) -> typing.Union[MetaOapg.properties.txnAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["firstName", "lastName", "middleName", "number", "issuedDate", "txnAmount", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        firstName: typing.Union[MetaOapg.properties.firstName, str, schemas.Unset] = schemas.unset,
        lastName: typing.Union[MetaOapg.properties.lastName, str, schemas.Unset] = schemas.unset,
        middleName: typing.Union[MetaOapg.properties.middleName, str, schemas.Unset] = schemas.unset,
        number: typing.Union[MetaOapg.properties.number, str, schemas.Unset] = schemas.unset,
        issuedDate: typing.Union[MetaOapg.properties.issuedDate, str, schemas.Unset] = schemas.unset,
        txnAmount: typing.Union[MetaOapg.properties.txnAmount, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ApplicantAddPaymentMethodInformationRequestDataRequiredIdDoc':
        return super().__new__(
            cls,
            *args,
            firstName=firstName,
            lastName=lastName,
            middleName=middleName,
            number=number,
            issuedDate=issuedDate,
            txnAmount=txnAmount,
            _configuration=_configuration,
            **kwargs,
        )
