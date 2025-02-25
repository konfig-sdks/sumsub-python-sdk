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

from sumsub_python_sdk.model.applicant_update_top_level_info_request_questionnaires import ApplicantUpdateTopLevelInfoRequestQuestionnaires as ApplicantUpdateTopLevelInfoRequestQuestionnairesSchema
from sumsub_python_sdk.model.applicant_update_top_level_info_request_metadata import ApplicantUpdateTopLevelInfoRequestMetadata as ApplicantUpdateTopLevelInfoRequestMetadataSchema
from sumsub_python_sdk.model.applicant_update_top_level_info_request import ApplicantUpdateTopLevelInfoRequest as ApplicantUpdateTopLevelInfoRequestSchema
from sumsub_python_sdk.model.applicant_update_top_level_info_request1 import ApplicantUpdateTopLevelInfoRequest1 as ApplicantUpdateTopLevelInfoRequest1Schema

from sumsub_python_sdk.type.applicant_update_top_level_info_request_questionnaires import ApplicantUpdateTopLevelInfoRequestQuestionnaires
from sumsub_python_sdk.type.applicant_update_top_level_info_request_metadata import ApplicantUpdateTopLevelInfoRequestMetadata
from sumsub_python_sdk.type.applicant_update_top_level_info_request1 import ApplicantUpdateTopLevelInfoRequest1
from sumsub_python_sdk.type.applicant_update_top_level_info_request import ApplicantUpdateTopLevelInfoRequest

from ...api_client import Dictionary
from sumsub_python_sdk.pydantic.applicant_update_top_level_info_request1 import ApplicantUpdateTopLevelInfoRequest1 as ApplicantUpdateTopLevelInfoRequest1Pydantic
from sumsub_python_sdk.pydantic.applicant_update_top_level_info_request_questionnaires import ApplicantUpdateTopLevelInfoRequestQuestionnaires as ApplicantUpdateTopLevelInfoRequestQuestionnairesPydantic
from sumsub_python_sdk.pydantic.applicant_update_top_level_info_request_metadata import ApplicantUpdateTopLevelInfoRequestMetadata as ApplicantUpdateTopLevelInfoRequestMetadataPydantic
from sumsub_python_sdk.pydantic.applicant_update_top_level_info_request import ApplicantUpdateTopLevelInfoRequest as ApplicantUpdateTopLevelInfoRequestPydantic

# body param
SchemaForRequestBodyApplicationJson = ApplicantUpdateTopLevelInfoRequestSchema
SchemaForRequestBodyMultipartFormData = ApplicantUpdateTopLevelInfoRequest1Schema


request_body_applicant_update_top_level_info_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
        'multipart/form-data': api_client.MediaType(
            schema=SchemaForRequestBodyMultipartFormData),
    },
)


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


class BaseApi(api_client.Api):

    def _update_top_level_info_mapped_args(
        self,
        id: str,
        external_user_id: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        source_key: typing.Optional[str] = None,
        lang: typing.Optional[str] = None,
        questionnaires: typing.Optional[ApplicantUpdateTopLevelInfoRequestQuestionnaires] = None,
        metadata: typing.Optional[ApplicantUpdateTopLevelInfoRequestMetadata] = None,
        deleted: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if id is not None:
            _body["id"] = id
        if external_user_id is not None:
            _body["externalUserId"] = external_user_id
        if email is not None:
            _body["email"] = email
        if phone is not None:
            _body["phone"] = phone
        if source_key is not None:
            _body["sourceKey"] = source_key
        if lang is not None:
            _body["lang"] = lang
        if questionnaires is not None:
            _body["questionnaires"] = questionnaires
        if metadata is not None:
            _body["metadata"] = metadata
        if deleted is not None:
            _body["deleted"] = deleted
        args.body = _body
        return args

    async def _aupdate_top_level_info_oapg(
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
        Change top-level information
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
            path_template='/resources/applicants',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_applicant_update_top_level_info_request.serialize(body, content_type)
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


    def _update_top_level_info_oapg(
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
        Change top-level information
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
            path_template='/resources/applicants',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_applicant_update_top_level_info_request.serialize(body, content_type)
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


class UpdateTopLevelInfoRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_top_level_info(
        self,
        id: str,
        external_user_id: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        source_key: typing.Optional[str] = None,
        lang: typing.Optional[str] = None,
        questionnaires: typing.Optional[ApplicantUpdateTopLevelInfoRequestQuestionnaires] = None,
        metadata: typing.Optional[ApplicantUpdateTopLevelInfoRequestMetadata] = None,
        deleted: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_top_level_info_mapped_args(
            id=id,
            external_user_id=external_user_id,
            email=email,
            phone=phone,
            source_key=source_key,
            lang=lang,
            questionnaires=questionnaires,
            metadata=metadata,
            deleted=deleted,
        )
        return await self._aupdate_top_level_info_oapg(
            body=args.body,
            **kwargs,
        )
    
    def update_top_level_info(
        self,
        id: str,
        external_user_id: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        source_key: typing.Optional[str] = None,
        lang: typing.Optional[str] = None,
        questionnaires: typing.Optional[ApplicantUpdateTopLevelInfoRequestQuestionnaires] = None,
        metadata: typing.Optional[ApplicantUpdateTopLevelInfoRequestMetadata] = None,
        deleted: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_top_level_info_mapped_args(
            id=id,
            external_user_id=external_user_id,
            email=email,
            phone=phone,
            source_key=source_key,
            lang=lang,
            questionnaires=questionnaires,
            metadata=metadata,
            deleted=deleted,
        )
        return self._update_top_level_info_oapg(
            body=args.body,
        )

class UpdateTopLevelInfo(BaseApi):

    async def aupdate_top_level_info(
        self,
        id: str,
        external_user_id: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        source_key: typing.Optional[str] = None,
        lang: typing.Optional[str] = None,
        questionnaires: typing.Optional[ApplicantUpdateTopLevelInfoRequestQuestionnaires] = None,
        metadata: typing.Optional[ApplicantUpdateTopLevelInfoRequestMetadata] = None,
        deleted: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.aupdate_top_level_info(
            id=id,
            external_user_id=external_user_id,
            email=email,
            phone=phone,
            source_key=source_key,
            lang=lang,
            questionnaires=questionnaires,
            metadata=metadata,
            deleted=deleted,
            **kwargs,
        )
    
    
    def update_top_level_info(
        self,
        id: str,
        external_user_id: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        source_key: typing.Optional[str] = None,
        lang: typing.Optional[str] = None,
        questionnaires: typing.Optional[ApplicantUpdateTopLevelInfoRequestQuestionnaires] = None,
        metadata: typing.Optional[ApplicantUpdateTopLevelInfoRequestMetadata] = None,
        deleted: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.update_top_level_info(
            id=id,
            external_user_id=external_user_id,
            email=email,
            phone=phone,
            source_key=source_key,
            lang=lang,
            questionnaires=questionnaires,
            metadata=metadata,
            deleted=deleted,
        )


class ApiForpatch(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apatch(
        self,
        id: str,
        external_user_id: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        source_key: typing.Optional[str] = None,
        lang: typing.Optional[str] = None,
        questionnaires: typing.Optional[ApplicantUpdateTopLevelInfoRequestQuestionnaires] = None,
        metadata: typing.Optional[ApplicantUpdateTopLevelInfoRequestMetadata] = None,
        deleted: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_top_level_info_mapped_args(
            id=id,
            external_user_id=external_user_id,
            email=email,
            phone=phone,
            source_key=source_key,
            lang=lang,
            questionnaires=questionnaires,
            metadata=metadata,
            deleted=deleted,
        )
        return await self._aupdate_top_level_info_oapg(
            body=args.body,
            **kwargs,
        )
    
    def patch(
        self,
        id: str,
        external_user_id: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        source_key: typing.Optional[str] = None,
        lang: typing.Optional[str] = None,
        questionnaires: typing.Optional[ApplicantUpdateTopLevelInfoRequestQuestionnaires] = None,
        metadata: typing.Optional[ApplicantUpdateTopLevelInfoRequestMetadata] = None,
        deleted: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_top_level_info_mapped_args(
            id=id,
            external_user_id=external_user_id,
            email=email,
            phone=phone,
            source_key=source_key,
            lang=lang,
            questionnaires=questionnaires,
            metadata=metadata,
            deleted=deleted,
        )
        return self._update_top_level_info_oapg(
            body=args.body,
        )

