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


class ApplicantSubmitTransactionDataRequest1CounterpartyDeviceAddress(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Device address.
    """


    class MetaOapg:
        
        class properties:
            country = schemas.StrSchema
            postCode = schemas.StrSchema
            town = schemas.StrSchema
            street = schemas.StrSchema
            subStreet = schemas.StrSchema
            state = schemas.StrSchema
            buildingName = schemas.StrSchema
            flatNumber = schemas.StrSchema
            buildingNumber = schemas.StrSchema
            __annotations__ = {
                "country": country,
                "postCode": postCode,
                "town": town,
                "street": street,
                "subStreet": subStreet,
                "state": state,
                "buildingName": buildingName,
                "flatNumber": flatNumber,
                "buildingNumber": buildingNumber,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country"]) -> MetaOapg.properties.country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["postCode"]) -> MetaOapg.properties.postCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["town"]) -> MetaOapg.properties.town: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["street"]) -> MetaOapg.properties.street: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subStreet"]) -> MetaOapg.properties.subStreet: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["buildingName"]) -> MetaOapg.properties.buildingName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["flatNumber"]) -> MetaOapg.properties.flatNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["buildingNumber"]) -> MetaOapg.properties.buildingNumber: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["country", "postCode", "town", "street", "subStreet", "state", "buildingName", "flatNumber", "buildingNumber", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country"]) -> typing.Union[MetaOapg.properties.country, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["postCode"]) -> typing.Union[MetaOapg.properties.postCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["town"]) -> typing.Union[MetaOapg.properties.town, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["street"]) -> typing.Union[MetaOapg.properties.street, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subStreet"]) -> typing.Union[MetaOapg.properties.subStreet, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union[MetaOapg.properties.state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["buildingName"]) -> typing.Union[MetaOapg.properties.buildingName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["flatNumber"]) -> typing.Union[MetaOapg.properties.flatNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["buildingNumber"]) -> typing.Union[MetaOapg.properties.buildingNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["country", "postCode", "town", "street", "subStreet", "state", "buildingName", "flatNumber", "buildingNumber", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        country: typing.Union[MetaOapg.properties.country, str, schemas.Unset] = schemas.unset,
        postCode: typing.Union[MetaOapg.properties.postCode, str, schemas.Unset] = schemas.unset,
        town: typing.Union[MetaOapg.properties.town, str, schemas.Unset] = schemas.unset,
        street: typing.Union[MetaOapg.properties.street, str, schemas.Unset] = schemas.unset,
        subStreet: typing.Union[MetaOapg.properties.subStreet, str, schemas.Unset] = schemas.unset,
        state: typing.Union[MetaOapg.properties.state, str, schemas.Unset] = schemas.unset,
        buildingName: typing.Union[MetaOapg.properties.buildingName, str, schemas.Unset] = schemas.unset,
        flatNumber: typing.Union[MetaOapg.properties.flatNumber, str, schemas.Unset] = schemas.unset,
        buildingNumber: typing.Union[MetaOapg.properties.buildingNumber, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ApplicantSubmitTransactionDataRequest1CounterpartyDeviceAddress':
        return super().__new__(
            cls,
            *args,
            country=country,
            postCode=postCode,
            town=town,
            street=street,
            subStreet=subStreet,
            state=state,
            buildingName=buildingName,
            flatNumber=flatNumber,
            buildingNumber=buildingNumber,
            _configuration=_configuration,
            **kwargs,
        )
