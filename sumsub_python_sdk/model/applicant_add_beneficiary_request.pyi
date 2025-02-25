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


class ApplicantAddBeneficiaryRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "applicantId",
            "type",
            "applicant",
        }
        
        class properties:
        
            @staticmethod
            def applicant() -> typing.Type['ApplicantAddBeneficiaryRequestApplicant']:
                return ApplicantAddBeneficiaryRequestApplicant
            applicantId = schemas.StrSchema
            type = schemas.StrSchema
        
            @staticmethod
            def positions() -> typing.Type['ApplicantAddBeneficiaryRequestPositions']:
                return ApplicantAddBeneficiaryRequestPositions
            __annotations__ = {
                "applicant": applicant,
                "applicantId": applicantId,
                "type": type,
                "positions": positions,
            }
    
    applicantId: MetaOapg.properties.applicantId
    type: MetaOapg.properties.type
    applicant: 'ApplicantAddBeneficiaryRequestApplicant'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["applicant"]) -> 'ApplicantAddBeneficiaryRequestApplicant': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["applicantId"]) -> MetaOapg.properties.applicantId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["positions"]) -> 'ApplicantAddBeneficiaryRequestPositions': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["applicant", "applicantId", "type", "positions", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["applicant"]) -> 'ApplicantAddBeneficiaryRequestApplicant': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["applicantId"]) -> MetaOapg.properties.applicantId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["positions"]) -> typing.Union['ApplicantAddBeneficiaryRequestPositions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["applicant", "applicantId", "type", "positions", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        applicantId: typing.Union[MetaOapg.properties.applicantId, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        applicant: 'ApplicantAddBeneficiaryRequestApplicant',
        positions: typing.Union['ApplicantAddBeneficiaryRequestPositions', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ApplicantAddBeneficiaryRequest':
        return super().__new__(
            cls,
            *args,
            applicantId=applicantId,
            type=type,
            applicant=applicant,
            positions=positions,
            _configuration=_configuration,
            **kwargs,
        )

from sumsub_python_sdk.model.applicant_add_beneficiary_request_applicant import ApplicantAddBeneficiaryRequestApplicant
from sumsub_python_sdk.model.applicant_add_beneficiary_request_positions import ApplicantAddBeneficiaryRequestPositions
