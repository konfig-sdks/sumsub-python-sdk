# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from sumsub_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    APPLICANT = "Applicant"
    TRANSACTION = "Transaction"
    CHECK = "Check"
    NOTE = "Note"
    TOKEN = "Token"
    IMAGE = "Image"
    VASP = "VASP"
    HEALTH = "Health"
    AUDIT_TRAIL_EVENT = "AuditTrailEvent"
    TAG = "Tag"
    ANALYSIS = "Analysis"
    WEB_SDKLINK = "WebSDKLink"
    INSPECTION = "Inspection"
