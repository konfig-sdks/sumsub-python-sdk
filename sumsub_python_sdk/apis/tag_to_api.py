import typing_extensions

from sumsub_python_sdk.apis.tags import TagValues
from sumsub_python_sdk.apis.tags.applicant_api import ApplicantApi
from sumsub_python_sdk.apis.tags.transaction_api import TransactionApi
from sumsub_python_sdk.apis.tags.check_api import CheckApi
from sumsub_python_sdk.apis.tags.note_api import NoteApi
from sumsub_python_sdk.apis.tags.token_api import TokenApi
from sumsub_python_sdk.apis.tags.image_api import ImageApi
from sumsub_python_sdk.apis.tags.vasp_api import VASPApi
from sumsub_python_sdk.apis.tags.health_api import HealthApi
from sumsub_python_sdk.apis.tags.audit_trail_event_api import AuditTrailEventApi
from sumsub_python_sdk.apis.tags.tag_api import TagApi
from sumsub_python_sdk.apis.tags.analysis_api import AnalysisApi
from sumsub_python_sdk.apis.tags.web_sdk_link_api import WebSDKLinkApi
from sumsub_python_sdk.apis.tags.inspection_api import InspectionApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.APPLICANT: ApplicantApi,
        TagValues.TRANSACTION: TransactionApi,
        TagValues.CHECK: CheckApi,
        TagValues.NOTE: NoteApi,
        TagValues.TOKEN: TokenApi,
        TagValues.IMAGE: ImageApi,
        TagValues.VASP: VASPApi,
        TagValues.HEALTH: HealthApi,
        TagValues.AUDIT_TRAIL_EVENT: AuditTrailEventApi,
        TagValues.TAG: TagApi,
        TagValues.ANALYSIS: AnalysisApi,
        TagValues.WEB_SDKLINK: WebSDKLinkApi,
        TagValues.INSPECTION: InspectionApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.APPLICANT: ApplicantApi,
        TagValues.TRANSACTION: TransactionApi,
        TagValues.CHECK: CheckApi,
        TagValues.NOTE: NoteApi,
        TagValues.TOKEN: TokenApi,
        TagValues.IMAGE: ImageApi,
        TagValues.VASP: VASPApi,
        TagValues.HEALTH: HealthApi,
        TagValues.AUDIT_TRAIL_EVENT: AuditTrailEventApi,
        TagValues.TAG: TagApi,
        TagValues.ANALYSIS: AnalysisApi,
        TagValues.WEB_SDKLINK: WebSDKLinkApi,
        TagValues.INSPECTION: InspectionApi,
    }
)
