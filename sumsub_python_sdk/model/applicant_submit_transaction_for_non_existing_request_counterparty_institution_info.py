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


class ApplicantSubmitTransactionForNonExistingRequestCounterpartyInstitutionInfo(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Transaction institution information
    """


    class MetaOapg:
        
        class properties:
            code = schemas.StrSchema
            name = schemas.StrSchema
        
            @staticmethod
            def address() -> typing.Type['ApplicantSubmitTransactionForNonExistingRequestCounterpartyInstitutionInfoAddress']:
                return ApplicantSubmitTransactionForNonExistingRequestCounterpartyInstitutionInfoAddress
            internalId = schemas.StrSchema
            __annotations__ = {
                "code": code,
                "name": name,
                "address": address,
                "internalId": internalId,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address"]) -> 'ApplicantSubmitTransactionForNonExistingRequestCounterpartyInstitutionInfoAddress': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["internalId"]) -> MetaOapg.properties.internalId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["code", "name", "address", "internalId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["code"]) -> typing.Union[MetaOapg.properties.code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> typing.Union['ApplicantSubmitTransactionForNonExistingRequestCounterpartyInstitutionInfoAddress', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["internalId"]) -> typing.Union[MetaOapg.properties.internalId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["code", "name", "address", "internalId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        code: typing.Union[MetaOapg.properties.code, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        address: typing.Union['ApplicantSubmitTransactionForNonExistingRequestCounterpartyInstitutionInfoAddress', schemas.Unset] = schemas.unset,
        internalId: typing.Union[MetaOapg.properties.internalId, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ApplicantSubmitTransactionForNonExistingRequestCounterpartyInstitutionInfo':
        return super().__new__(
            cls,
            *args,
            code=code,
            name=name,
            address=address,
            internalId=internalId,
            _configuration=_configuration,
            **kwargs,
        )

from sumsub_python_sdk.model.applicant_submit_transaction_for_non_existing_request_counterparty_institution_info_address import ApplicantSubmitTransactionForNonExistingRequestCounterpartyInstitutionInfoAddress
