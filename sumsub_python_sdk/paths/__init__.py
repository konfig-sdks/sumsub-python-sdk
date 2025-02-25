# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from sumsub_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    RESOURCES_STATUS_API = "/resources/status/api"
    RESOURCES_APPLICANTS = "/resources/applicants"
    RESOURCES_APPLICANTS_APPLICANT_ID_MOVE_TO_LEVEL = "/resources/applicants/{applicantId}/moveToLevel"
    RESOURCES_APPLICANTS_APPLICANT_ID_REQUIRED_ID_DOCS = "/resources/applicants/{applicantId}/requiredIdDocs"
    RESOURCES_APPLICANTS_APPLICANT_ID_INFO_ID_DOC = "/resources/applicants/{applicantId}/info/idDoc"
    RESOURCES_APPLICANTS_APPLICANT_ID_FIXED_INFO = "/resources/applicants/{applicantId}/fixedInfo"
    RESOURCES_APPLICANTS_APPLICANT_ID_INFO = "/resources/applicants/{applicantId}/info"
    RESOURCES_APPLICANTS__INGEST_COMPLETEDLEVEL_NAMELEVEL_NAME = "/resources/applicants/-/ingestCompleted?levelName&#x3D;{levelName}"
    RESOURCES_APPLICANTS__APPLICANT_IMPORT = "/resources/applicants/-/applicantImport"
    RESOURCES_APPLICANTS_APPLICANT_ID_STATUS_TEST_COMPLETED = "/resources/applicants/{applicantId}/status/testCompleted"
    RESOURCES_APPLICANTS_APPLICANT_ID_TAGS_ADD = "/resources/applicants/{applicantId}/tags/add"
    RESOURCES_APPLICANTS_APPLICANT_ID_TAGS = "/resources/applicants/{applicantId}/tags"
    RESOURCES_APPLICANTS_APPLICANT_ID_STATUS_PENDINGREASONREASON = "/resources/applicants/{applicantId}/status/pending?reason&#x3D;{reason}"
    RESOURCES_APPLICANTS_APPLICANT_ID_BLACKLISTNOTENOTE = "/resources/applicants/{applicantId}/blacklist?note&#x3D;{note}"
    RESOURCES_APPLICANTS_APPLICANT_ID_RESET = "/resources/applicants/{applicantId}/reset"
    RESOURCES_APPLICANTS_APPLICANT_ID_RESET_STEP_ID_DOC_SET_TYPE = "/resources/applicants/{applicantId}/resetStep/{idDocSetType}"
    RESOURCES_INSPECTIONS_INSPECTION_ID_RESOURCES_IMAGE_ID = "/resources/inspections/{inspectionId}/resources/{imageId}"
    RESOURCES_APPLICANTS_APPLICANT_ID_PRESENCE_STATUS = "/resources/applicants/{applicantId}/presence/{status}"
    RESOURCES_APPLICANTS_APPLICANT_ID_AGREEMENT = "/resources/applicants/{applicantId}/agreement"
    RESOURCES_APPLICANTS_APPLICANT_ID_ONE = "/resources/applicants/{applicantId}/one"
    RESOURCES_APPLICANTS_EXTERNAL_USER_IDEXTERNAL_USER_ID_ONE = "/resources/applicants/-;externalUserId&#x3D;{externalUserId}/one"
    RESOURCES_APPLICANTS_APPLICANT_ID_STATUS = "/resources/applicants/{applicantId}/status"
    RESOURCES_APPLICANTS_APPLICANT_ID_REQUIRED_ID_DOCS_STATUS = "/resources/applicants/{applicantId}/requiredIdDocsStatus"
    RESOURCES_MODERATION_STATES_APPLICANT_IDAPPLICANT_ID = "/resources/moderationStates/-;applicantId&#x3D;{applicantId}"
    RESOURCES_CHECKS_LATESTTYPETIN = "/resources/checks/latest?type&#x3D;TIN"
    RESOURCES_CHECKS_LATESTTYPEEMAIL_CONFIRMATION = "/resources/checks/latest?type&#x3D;EMAIL_CONFIRMATION"
    RESOURCES_CHECKS_LATESTTYPEPHONE_CONFIRMATION = "/resources/checks/latest?type&#x3D;PHONE_CONFIRMATION"
    RESOURCES_CHECKS_LATESTTYPEIP_CHECK = "/resources/checks/latest?type&#x3D;IP_CHECK"
    RESOURCES_APPLICANT_FRAUD_NETWORKS__BY_APPLICANT_APPLICANT_ID = "/resources/applicantFraudNetworks/-/byApplicant/{applicantId}"
    RESOURCES_APPLICANT_FRAUD_NETWORKS_NETWORK_ID_ONE = "/resources/applicantFraudNetworks/{networkId}/one"
    RESOURCES_CHECKS_CROSS_CHECKCOMPARISON_MODECOMPARISON_MODE = "/resources/checks/crossCheck?comparisonMode&#x3D;{comparisonMode}"
    RESOURCES_SDK_INTEGRATIONS_LEVELS_LEVEL_NAME_WEBSDK_LINK = "/resources/sdkIntegrations/levels/{levelName}/websdkLink"
    RESOURCES_APPLICANTS__LEVELS = "/resources/applicants/-/levels"
    RESOURCES_CHECKS_LATESTTYPEPOA = "/resources/checks/latest?type&#x3D;POA"
    RESOURCES_ACCESS_TOKENS = "/resources/accessTokens"
    RESOURCES_APPLICANT_ACTIONS_APPLICANT_IDAPPLICANT_ID = "/resources/applicantActions/-;applicantId&#x3D;{applicantId}"
    RESOURCES_APPLICANT_ACTIONS_ACTION_ID_ONE = "/resources/applicantActions/{actionId}/one"
    RESOURCES_APPLICANT_ACTIONS__FOR_APPLICANT_APPLICANT_IDLEVEL_NAMELEVEL_NAME = "/resources/applicantActions/-/forApplicant/{applicantId}?levelName&#x3D;{levelName}"
    RESOURCES_APPLICANT_ACTIONS__FOR_APPLICANT_APPLICANT_ID_LEVEL_NAMEPAYMENT_SOURCE = "/resources/applicantActions/-/forApplicant/{applicantId}/?levelName&#x3D;paymentSource"
    RESOURCES_APPLICANT_ACTIONS_ACTION_ID_REVIEW_STATUS_PENDING = "/resources/applicantActions/{actionId}/review/status/pending"
    RESOURCES_APPLICANT_ACTIONS__FOR_APPLICANT_APPLICANT_ID_PAYMENT_METHOD = "/resources/applicantActions/-/forApplicant/{applicantId}/paymentMethod"
    RESOURCES_APPLICANT_ACTIONS_ACTION_ID_PAYMENT_METHOD = "/resources/applicantActions/{actionId}/paymentMethod"
    RESOURCES_APPLICANT_ACTIONS_ACTION_ID_IMAGES_IMAGE_IDPREVIEWIS_PREVIEW = "/resources/applicantActions/{actionId}/images/{imageId}?preview&#x3D;{isPreview}"
    RESOURCES_APPLICANT_ACTIONS_ACTION_ID_IMAGES = "/resources/applicantActions/{actionId}/images"
    RESOURCES_APPLICANT_ACTIONS__FOR_APPLICANT_APPLICANT_ID_CRYPTO_SOURCE_OF_FUNDS = "/resources/applicantActions/-/forApplicant/{applicantId}/cryptoSourceOfFunds"
    RESOURCES_STANDALONE_CRYPTO_CRYPTO_SOURCE_OF_FUNDS = "/resources/standalone/crypto/cryptoSourceOfFunds"
    RESOURCES_STANDALONE_CRYPTO_AVAILABLE_CURRENCIES = "/resources/standalone/crypto/availableCurrencies"
    RESOURCES_APPLICANTS_APPLICANT_ID_INFO_COMPANY_INFO_BENEFICIARIES = "/resources/applicants/{applicantId}/info/companyInfo/beneficiaries"
    RESOURCES_APPLICANTS_APPLICANT_ID_INFO_COMPANY_INFO_BENEFICIARIES_BENEFICIARY_APPLICANT_ID = "/resources/applicants/{applicantId}/info/companyInfo/beneficiaries/{beneficiaryApplicantId}"
    RESOURCES_APPLICANTS_APPLICANT_ID_INFO_COMPANY_INFO = "/resources/applicants/{applicantId}/info/companyInfo"
    RESOURCES_CHECKS_LATESTTYPECOMPANY = "/resources/checks/latest?type&#x3D;COMPANY"
    RESOURCES_INSPECTIONS_INSPECTION_IDFIELDSVIDEO_IDENT_DATA = "/resources/inspections/{inspectionId}?fields&#x3D;videoIdentData"
    RESOURCES_VIDEO_IDENT_APPLICANT_APPLICANT_ID_MEDIA_COMPOSITION_MEDIA_ID = "/resources/videoIdent/applicant/{applicantId}/media/{compositionMediaId}"
    RESOURCES_APPLICANTS_APPLICANT_ID_EKYC_SUBMIT = "/resources/applicants/{applicantId}/ekyc/submit"
    RESOURCES_APPLICANTS_APPLICANT_ID_EKYC_CONFIRM_CONFIRMATIONID = "/resources/applicants/{applicantId}/ekyc/confirm/{confirmationid}"
    RESOURCES_CHECKS_LATEST = "/resources/checks/latest"
    RESOURCES_APPLICANTS_APPLICANT_ID_KYT_TXNS__DATA = "/resources/applicants/{applicantId}/kyt/txns/-/data"
    RESOURCES_APPLICANTS__KYT_TXNS__DATA = "/resources/applicants/-/kyt/txns/-/data"
    RESOURCES_KYT_TXNS_ID_ONE = "/resources/kyt/txns/{id}/one"
    RESOURCES_KYT_TXNS_DATA_TXN_IDEXTERNAL_TXN_ID_ONE = "/resources/kyt/txns/-;data.txnId&#x3D;{externalTxnId}/one"
    RESOURCES_KYT_MISC_TXNS_IMPORT = "/resources/kyt/misc/txns/import"
    RESOURCES_KYT_TXNS_ID_PROPS = "/resources/kyt/txns/{id}/props"
    RESOURCES_KYT_TXNS_ID__SCORE = "/resources/kyt/txns/{id}/-/score"
    RESOURCES_KYT_TXNS_ID_REVIEW_STATUS_COMPLETED = "/resources/kyt/txns/{id}/review/status/completed"
    RESOURCES_KYT_TXNS_ID_TAGS = "/resources/kyt/txns/{id}/tags"
    RESOURCES_KYT_TXNS_ID_NOTES = "/resources/kyt/txns/{id}/notes"
    RESOURCES_KYT_TXNS_NOTES = "/resources/kyt/txns/notes"
    RESOURCES_KYT_TXNS_TXN_ID_DATA_INFO = "/resources/kyt/txns/{txnId}/data/info"
    RESOURCES_KYT_TXNS_TXN_ID_APPLICANT_ID_APPLICANT_ID = "/resources/kyt/txns/{txnId}/applicantId/{applicantId}"
    RESOURCES_KYT_TXNS_TXN_ID_DATA_APPLICANT = "/resources/kyt/txns/{txnId}/data/applicant"
    RESOURCES_KYT_TXNS_TXN_ID_OWNERSHIP_CONFIRMED = "/resources/kyt/txns/{txnId}/ownership/confirmed"
    RESOURCES_KYT_TXNS_TXN_ID_OWNERSHIP_UNCONFIRMED = "/resources/kyt/txns/{txnId}/ownership/unconfirmed"
    RESOURCES_VASPS_ = "/resources/vasps/-"
    RESOURCES_AUDIT_TRAIL_EVENTS = "/resources/auditTrailEvents"
    RESOURCES_APPLICANT_FRAUD_NETWORKS = "/resources/applicantFraudNetworks"
