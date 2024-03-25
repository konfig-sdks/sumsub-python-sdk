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


class ApplicantSubmitTransactionForNonExistingRequestCounterpartyDevice(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Device information.
    """


    class MetaOapg:
        
        class properties:
            userAgent = schemas.StrSchema
            sessionId = schemas.StrSchema
            sessionAgeMs = schemas.Int64Schema
            acceptLang = schemas.StrSchema
            platform = schemas.StrSchema
            fingerprint = schemas.StrSchema
        
            @staticmethod
            def address() -> typing.Type['ApplicantSubmitTransactionForNonExistingRequestCounterpartyDeviceAddress']:
                return ApplicantSubmitTransactionForNonExistingRequestCounterpartyDeviceAddress
        
            @staticmethod
            def coords() -> typing.Type['ApplicantSubmitTransactionForNonExistingRequestCounterpartyDeviceCoords']:
                return ApplicantSubmitTransactionForNonExistingRequestCounterpartyDeviceCoords
        
            @staticmethod
            def ipInfo() -> typing.Type['ApplicantSubmitTransactionForNonExistingRequestCounterpartyDeviceIpInfo']:
                return ApplicantSubmitTransactionForNonExistingRequestCounterpartyDeviceIpInfo
            __annotations__ = {
                "userAgent": userAgent,
                "sessionId": sessionId,
                "sessionAgeMs": sessionAgeMs,
                "acceptLang": acceptLang,
                "platform": platform,
                "fingerprint": fingerprint,
                "address": address,
                "coords": coords,
                "ipInfo": ipInfo,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userAgent"]) -> MetaOapg.properties.userAgent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sessionId"]) -> MetaOapg.properties.sessionId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sessionAgeMs"]) -> MetaOapg.properties.sessionAgeMs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["acceptLang"]) -> MetaOapg.properties.acceptLang: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["platform"]) -> MetaOapg.properties.platform: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fingerprint"]) -> MetaOapg.properties.fingerprint: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address"]) -> 'ApplicantSubmitTransactionForNonExistingRequestCounterpartyDeviceAddress': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["coords"]) -> 'ApplicantSubmitTransactionForNonExistingRequestCounterpartyDeviceCoords': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ipInfo"]) -> 'ApplicantSubmitTransactionForNonExistingRequestCounterpartyDeviceIpInfo': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["userAgent", "sessionId", "sessionAgeMs", "acceptLang", "platform", "fingerprint", "address", "coords", "ipInfo", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userAgent"]) -> typing.Union[MetaOapg.properties.userAgent, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sessionId"]) -> typing.Union[MetaOapg.properties.sessionId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sessionAgeMs"]) -> typing.Union[MetaOapg.properties.sessionAgeMs, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["acceptLang"]) -> typing.Union[MetaOapg.properties.acceptLang, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["platform"]) -> typing.Union[MetaOapg.properties.platform, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fingerprint"]) -> typing.Union[MetaOapg.properties.fingerprint, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> typing.Union['ApplicantSubmitTransactionForNonExistingRequestCounterpartyDeviceAddress', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["coords"]) -> typing.Union['ApplicantSubmitTransactionForNonExistingRequestCounterpartyDeviceCoords', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ipInfo"]) -> typing.Union['ApplicantSubmitTransactionForNonExistingRequestCounterpartyDeviceIpInfo', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["userAgent", "sessionId", "sessionAgeMs", "acceptLang", "platform", "fingerprint", "address", "coords", "ipInfo", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        userAgent: typing.Union[MetaOapg.properties.userAgent, str, schemas.Unset] = schemas.unset,
        sessionId: typing.Union[MetaOapg.properties.sessionId, str, schemas.Unset] = schemas.unset,
        sessionAgeMs: typing.Union[MetaOapg.properties.sessionAgeMs, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        acceptLang: typing.Union[MetaOapg.properties.acceptLang, str, schemas.Unset] = schemas.unset,
        platform: typing.Union[MetaOapg.properties.platform, str, schemas.Unset] = schemas.unset,
        fingerprint: typing.Union[MetaOapg.properties.fingerprint, str, schemas.Unset] = schemas.unset,
        address: typing.Union['ApplicantSubmitTransactionForNonExistingRequestCounterpartyDeviceAddress', schemas.Unset] = schemas.unset,
        coords: typing.Union['ApplicantSubmitTransactionForNonExistingRequestCounterpartyDeviceCoords', schemas.Unset] = schemas.unset,
        ipInfo: typing.Union['ApplicantSubmitTransactionForNonExistingRequestCounterpartyDeviceIpInfo', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ApplicantSubmitTransactionForNonExistingRequestCounterpartyDevice':
        return super().__new__(
            cls,
            *args,
            userAgent=userAgent,
            sessionId=sessionId,
            sessionAgeMs=sessionAgeMs,
            acceptLang=acceptLang,
            platform=platform,
            fingerprint=fingerprint,
            address=address,
            coords=coords,
            ipInfo=ipInfo,
            _configuration=_configuration,
            **kwargs,
        )

from sumsub_python_sdk.model.applicant_submit_transaction_for_non_existing_request_counterparty_device_address import ApplicantSubmitTransactionForNonExistingRequestCounterpartyDeviceAddress
from sumsub_python_sdk.model.applicant_submit_transaction_for_non_existing_request_counterparty_device_coords import ApplicantSubmitTransactionForNonExistingRequestCounterpartyDeviceCoords
from sumsub_python_sdk.model.applicant_submit_transaction_for_non_existing_request_counterparty_device_ip_info import ApplicantSubmitTransactionForNonExistingRequestCounterpartyDeviceIpInfo
