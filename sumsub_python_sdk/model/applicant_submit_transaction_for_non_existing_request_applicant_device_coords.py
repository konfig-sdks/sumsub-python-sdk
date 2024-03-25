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


class ApplicantSubmitTransactionForNonExistingRequestApplicantDeviceCoords(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Coordinates.
    """


    class MetaOapg:
        
        class properties:
            lat = schemas.Float64Schema
            lon = schemas.Float64Schema
            accuracy = schemas.StrSchema
            __annotations__ = {
                "lat": lat,
                "lon": lon,
                "accuracy": accuracy,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lat"]) -> MetaOapg.properties.lat: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lon"]) -> MetaOapg.properties.lon: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accuracy"]) -> MetaOapg.properties.accuracy: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["lat", "lon", "accuracy", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lat"]) -> typing.Union[MetaOapg.properties.lat, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lon"]) -> typing.Union[MetaOapg.properties.lon, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accuracy"]) -> typing.Union[MetaOapg.properties.accuracy, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["lat", "lon", "accuracy", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        lat: typing.Union[MetaOapg.properties.lat, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        lon: typing.Union[MetaOapg.properties.lon, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        accuracy: typing.Union[MetaOapg.properties.accuracy, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ApplicantSubmitTransactionForNonExistingRequestApplicantDeviceCoords':
        return super().__new__(
            cls,
            *args,
            lat=lat,
            lon=lon,
            accuracy=accuracy,
            _configuration=_configuration,
            **kwargs,
        )
