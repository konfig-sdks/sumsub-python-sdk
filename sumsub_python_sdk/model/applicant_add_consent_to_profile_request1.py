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


class ApplicantAddConsentToProfileRequest1(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "records",
        }
        
        class properties:
        
            @staticmethod
            def records() -> typing.Type['ApplicantAddConsentToProfileRequest1Records']:
                return ApplicantAddConsentToProfileRequest1Records
            acceptedAt = schemas.StrSchema
            residenceCountry = schemas.StrSchema
            __annotations__ = {
                "records": records,
                "acceptedAt": acceptedAt,
                "residenceCountry": residenceCountry,
            }
    
    records: 'ApplicantAddConsentToProfileRequest1Records'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["records"]) -> 'ApplicantAddConsentToProfileRequest1Records': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["acceptedAt"]) -> MetaOapg.properties.acceptedAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["residenceCountry"]) -> MetaOapg.properties.residenceCountry: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["records", "acceptedAt", "residenceCountry", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["records"]) -> 'ApplicantAddConsentToProfileRequest1Records': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["acceptedAt"]) -> typing.Union[MetaOapg.properties.acceptedAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["residenceCountry"]) -> typing.Union[MetaOapg.properties.residenceCountry, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["records", "acceptedAt", "residenceCountry", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        records: 'ApplicantAddConsentToProfileRequest1Records',
        acceptedAt: typing.Union[MetaOapg.properties.acceptedAt, str, schemas.Unset] = schemas.unset,
        residenceCountry: typing.Union[MetaOapg.properties.residenceCountry, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ApplicantAddConsentToProfileRequest1':
        return super().__new__(
            cls,
            *args,
            records=records,
            acceptedAt=acceptedAt,
            residenceCountry=residenceCountry,
            _configuration=_configuration,
            **kwargs,
        )

from sumsub_python_sdk.model.applicant_add_consent_to_profile_request1_records import ApplicantAddConsentToProfileRequest1Records
