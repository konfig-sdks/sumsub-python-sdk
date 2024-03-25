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


class ApplicantAddPaymentMethodInformationRequest1(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "type",
        }
        
        class properties:
            type = schemas.StrSchema
            subType = schemas.StrSchema
        
            @staticmethod
            def data() -> typing.Type['ApplicantAddPaymentMethodInformationRequest1Data']:
                return ApplicantAddPaymentMethodInformationRequest1Data
            __annotations__ = {
                "type": type,
                "subType": subType,
                "data": data,
            }
    
    type: MetaOapg.properties.type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subType"]) -> MetaOapg.properties.subType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> 'ApplicantAddPaymentMethodInformationRequest1Data': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "subType", "data", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subType"]) -> typing.Union[MetaOapg.properties.subType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> typing.Union['ApplicantAddPaymentMethodInformationRequest1Data', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "subType", "data", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        subType: typing.Union[MetaOapg.properties.subType, str, schemas.Unset] = schemas.unset,
        data: typing.Union['ApplicantAddPaymentMethodInformationRequest1Data', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ApplicantAddPaymentMethodInformationRequest1':
        return super().__new__(
            cls,
            *args,
            type=type,
            subType=subType,
            data=data,
            _configuration=_configuration,
            **kwargs,
        )

from sumsub_python_sdk.model.applicant_add_payment_method_information_request1_data import ApplicantAddPaymentMethodInformationRequest1Data
