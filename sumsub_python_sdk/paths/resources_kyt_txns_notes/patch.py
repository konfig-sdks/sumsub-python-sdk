# coding: utf-8

"""
    Sumsub API

    Sumsub is the one verification platform to secure the whole user journey. With Sumsub's customizable KYC, KYB, transaction monitoring and fraud prevention solutions, you can orchestrate your verification process, welcome more customers worldwide, meet compliance requirements, reduce costs and protect your business.  Sumsub has over 2,000 clients in fintech, crypto, transportation, trading, e-commerce and gaming industries including Binance, Wirex, Avis, Bybit, Huobi, Unlimit, Flutter, Kaizen Gaming, and TransferGo.

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from sumsub_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from sumsub_python_sdk.api_response import AsyncGeneratorResponse
from sumsub_python_sdk import api_client, exceptions
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

from sumsub_python_sdk.model.note_update_transaction_notes_request_tags import NoteUpdateTransactionNotesRequestTags as NoteUpdateTransactionNotesRequestTagsSchema
from sumsub_python_sdk.model.note_update_transaction_notes_request1 import NoteUpdateTransactionNotesRequest1 as NoteUpdateTransactionNotesRequest1Schema
from sumsub_python_sdk.model.note_update_transaction_notes_request import NoteUpdateTransactionNotesRequest as NoteUpdateTransactionNotesRequestSchema

from sumsub_python_sdk.type.note_update_transaction_notes_request import NoteUpdateTransactionNotesRequest
from sumsub_python_sdk.type.note_update_transaction_notes_request1 import NoteUpdateTransactionNotesRequest1
from sumsub_python_sdk.type.note_update_transaction_notes_request_tags import NoteUpdateTransactionNotesRequestTags

from ...api_client import Dictionary
from sumsub_python_sdk.pydantic.note_update_transaction_notes_request import NoteUpdateTransactionNotesRequest as NoteUpdateTransactionNotesRequestPydantic
from sumsub_python_sdk.pydantic.note_update_transaction_notes_request_tags import NoteUpdateTransactionNotesRequestTags as NoteUpdateTransactionNotesRequestTagsPydantic
from sumsub_python_sdk.pydantic.note_update_transaction_notes_request1 import NoteUpdateTransactionNotesRequest1 as NoteUpdateTransactionNotesRequest1Pydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = NoteUpdateTransactionNotesRequestSchema
SchemaForRequestBodyMultipartFormData = NoteUpdateTransactionNotesRequest1Schema


request_body_note_update_transaction_notes_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
        'multipart/form-data': api_client.MediaType(
            schema=SchemaForRequestBodyMultipartFormData),
    },
)
_auth = [
    'sec0',
]


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
)
_status_code_to_response = {
    '200': _response_for_200,
}


class BaseApi(api_client.Api):

    def _update_transaction_notes_mapped_args(
        self,
        txn_id: str,
        id: str,
        note: str,
        tags: typing.Optional[NoteUpdateTransactionNotesRequestTags] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if tags is not None:
            _body["tags"] = tags
        if txn_id is not None:
            _body["txnId"] = txn_id
        if id is not None:
            _body["id"] = id
        if note is not None:
            _body["note"] = note
        args.body = _body
        return args

    async def _aupdate_transaction_notes_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Edit notes
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        method = 'patch'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/resources/kyt/txns/notes',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_note_update_transaction_notes_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _update_transaction_notes_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Edit notes
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        method = 'patch'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/resources/kyt/txns/notes',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_note_update_transaction_notes_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class UpdateTransactionNotesRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_transaction_notes(
        self,
        txn_id: str,
        id: str,
        note: str,
        tags: typing.Optional[NoteUpdateTransactionNotesRequestTags] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_transaction_notes_mapped_args(
            txn_id=txn_id,
            id=id,
            note=note,
            tags=tags,
        )
        return await self._aupdate_transaction_notes_oapg(
            body=args.body,
            **kwargs,
        )
    
    def update_transaction_notes(
        self,
        txn_id: str,
        id: str,
        note: str,
        tags: typing.Optional[NoteUpdateTransactionNotesRequestTags] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_transaction_notes_mapped_args(
            txn_id=txn_id,
            id=id,
            note=note,
            tags=tags,
        )
        return self._update_transaction_notes_oapg(
            body=args.body,
        )

class UpdateTransactionNotes(BaseApi):

    async def aupdate_transaction_notes(
        self,
        txn_id: str,
        id: str,
        note: str,
        tags: typing.Optional[NoteUpdateTransactionNotesRequestTags] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.aupdate_transaction_notes(
            txn_id=txn_id,
            id=id,
            note=note,
            tags=tags,
            **kwargs,
        )
    
    
    def update_transaction_notes(
        self,
        txn_id: str,
        id: str,
        note: str,
        tags: typing.Optional[NoteUpdateTransactionNotesRequestTags] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.update_transaction_notes(
            txn_id=txn_id,
            id=id,
            note=note,
            tags=tags,
        )


class ApiForpatch(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apatch(
        self,
        txn_id: str,
        id: str,
        note: str,
        tags: typing.Optional[NoteUpdateTransactionNotesRequestTags] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_transaction_notes_mapped_args(
            txn_id=txn_id,
            id=id,
            note=note,
            tags=tags,
        )
        return await self._aupdate_transaction_notes_oapg(
            body=args.body,
            **kwargs,
        )
    
    def patch(
        self,
        txn_id: str,
        id: str,
        note: str,
        tags: typing.Optional[NoteUpdateTransactionNotesRequestTags] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_transaction_notes_mapped_args(
            txn_id=txn_id,
            id=id,
            note=note,
            tags=tags,
        )
        return self._update_transaction_notes_oapg(
            body=args.body,
        )

