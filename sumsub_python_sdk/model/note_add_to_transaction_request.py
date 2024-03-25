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


class NoteAddToTransactionRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "note",
            "txnId",
        }
        
        class properties:
            txnId = schemas.StrSchema
            note = schemas.StrSchema
        
            @staticmethod
            def tags() -> typing.Type['NoteAddToTransactionRequestTags']:
                return NoteAddToTransactionRequestTags
            __annotations__ = {
                "txnId": txnId,
                "note": note,
                "tags": tags,
            }
    
    note: MetaOapg.properties.note
    txnId: MetaOapg.properties.txnId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["txnId"]) -> MetaOapg.properties.txnId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["note"]) -> MetaOapg.properties.note: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tags"]) -> 'NoteAddToTransactionRequestTags': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["txnId", "note", "tags", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["txnId"]) -> MetaOapg.properties.txnId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["note"]) -> MetaOapg.properties.note: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tags"]) -> typing.Union['NoteAddToTransactionRequestTags', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["txnId", "note", "tags", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        note: typing.Union[MetaOapg.properties.note, str, ],
        txnId: typing.Union[MetaOapg.properties.txnId, str, ],
        tags: typing.Union['NoteAddToTransactionRequestTags', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NoteAddToTransactionRequest':
        return super().__new__(
            cls,
            *args,
            note=note,
            txnId=txnId,
            tags=tags,
            _configuration=_configuration,
            **kwargs,
        )

from sumsub_python_sdk.model.note_add_to_transaction_request_tags import NoteAddToTransactionRequestTags
