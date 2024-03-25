# coding: utf-8
"""
    Sumsub API

    Sumsub is the one verification platform to secure the whole user journey. With Sumsub's customizable KYC, KYB, transaction monitoring and fraud prevention solutions, you can orchestrate your verification process, welcome more customers worldwide, meet compliance requirements, reduce costs and protect your business.  Sumsub has over 2,000 clients in fintech, crypto, transportation, trading, e-commerce and gaming industries including Binance, Wirex, Avis, Bybit, Huobi, Unlimit, Flutter, Kaizen Gaming, and TransferGo.

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

import typing
import inspect
from datetime import date, datetime
from sumsub_python_sdk.client_custom import ClientCustom
from sumsub_python_sdk.configuration import Configuration
from sumsub_python_sdk.api_client import ApiClient
from sumsub_python_sdk.type_util import copy_signature
from sumsub_python_sdk.apis.tags.analysis_api import AnalysisApi
from sumsub_python_sdk.apis.tags.applicant_api import ApplicantApi
from sumsub_python_sdk.apis.tags.audit_trail_event_api import AuditTrailEventApi
from sumsub_python_sdk.apis.tags.check_api import CheckApi
from sumsub_python_sdk.apis.tags.health_api import HealthApi
from sumsub_python_sdk.apis.tags.image_api import ImageApi
from sumsub_python_sdk.apis.tags.inspection_api import InspectionApi
from sumsub_python_sdk.apis.tags.note_api import NoteApi
from sumsub_python_sdk.apis.tags.tag_api import TagApi
from sumsub_python_sdk.apis.tags.token_api import TokenApi
from sumsub_python_sdk.apis.tags.transaction_api import TransactionApi
from sumsub_python_sdk.apis.tags.vasp_api import VASPApi
from sumsub_python_sdk.apis.tags.web_sdk_link_api import WebSDKLinkApi



class Sumsub(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.analysis: AnalysisApi = AnalysisApi(api_client)
        self.applicant: ApplicantApi = ApplicantApi(api_client)
        self.audit_trail_event: AuditTrailEventApi = AuditTrailEventApi(api_client)
        self.check: CheckApi = CheckApi(api_client)
        self.health: HealthApi = HealthApi(api_client)
        self.image: ImageApi = ImageApi(api_client)
        self.inspection: InspectionApi = InspectionApi(api_client)
        self.note: NoteApi = NoteApi(api_client)
        self.tag: TagApi = TagApi(api_client)
        self.token: TokenApi = TokenApi(api_client)
        self.transaction: TransactionApi = TransactionApi(api_client)
        self.vasp: VASPApi = VASPApi(api_client)
        self.web_sdk_link: WebSDKLinkApi = WebSDKLinkApi(api_client)
