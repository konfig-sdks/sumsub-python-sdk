# coding: utf-8

"""
    Sumsub API

    Sumsub is the one verification platform to secure the whole user journey. With Sumsub's customizable KYC, KYB, transaction monitoring and fraud prevention solutions, you can orchestrate your verification process, welcome more customers worldwide, meet compliance requirements, reduce costs and protect your business.  Sumsub has over 2,000 clients in fintech, crypto, transportation, trading, e-commerce and gaming industries including Binance, Wirex, Avis, Bybit, Huobi, Unlimit, Flutter, Kaizen Gaming, and TransferGo.

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict

from sumsub_python_sdk.pydantic.applicant_update_fixed_info_request_addresses import ApplicantUpdateFixedInfoRequestAddresses

class ApplicantUpdateFixedInfoRequest(BaseModel):
    # The first name of the applicant.
    first_name: typing.Optional[str] = Field(None, alias='firstName')

    # The last name of the applicant.
    last_name: typing.Optional[str] = Field(None, alias='lastName')

    # The middle name of the applicant.
    middle_name: typing.Optional[str] = Field(None, alias='middleName')

    # Automatic transliteration of the first name.
    first_name_en: typing.Optional[str] = Field(None, alias='firstNameEn')

    # Automatic transliteration of the last name.
    last_name_en: typing.Optional[str] = Field(None, alias='lastNameEn')

    # Automatic transliteration of the middle name.
    middle_name_en: typing.Optional[str] = Field(None, alias='middleNameEn')

    # Legal name.
    legal_name: typing.Optional[str] = Field(None, alias='legalName')

    # An applicant gender (`M` or `F`).
    gender: typing.Optional[str] = Field(None, alias='gender')

    # Applicant date of birth (format `YYYY-mm-dd`, e.g. 2001-09-25).
    dob: typing.Optional[str] = Field(None, alias='dob')

    # The applicant birthplace.
    place_of_birth: typing.Optional[str] = Field(None, alias='placeOfBirth')

    # Applicant country of birth.
    country_of_birth: typing.Optional[str] = Field(None, alias='countryOfBirth')

    # Applicant state of birth.
    state_of_birth: typing.Optional[str] = Field(None, alias='stateOfBirth')

    # Alpha-3 country code (e.g. `DEU` or `GBR`).
    country: typing.Optional[str] = Field(None, alias='country')

    # Alpha-3 country code.
    nationality: typing.Optional[str] = Field(None, alias='nationality')

    addresses: typing.Optional[ApplicantUpdateFixedInfoRequestAddresses] = Field(None, alias='addresses')

    # Tax identification number.
    tin: typing.Optional[str] = Field(None, alias='tin')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
