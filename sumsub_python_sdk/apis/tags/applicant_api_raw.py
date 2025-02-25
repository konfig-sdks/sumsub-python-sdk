# coding: utf-8

"""
    Sumsub API

    Sumsub is the one verification platform to secure the whole user journey. With Sumsub's customizable KYC, KYB, transaction monitoring and fraud prevention solutions, you can orchestrate your verification process, welcome more customers worldwide, meet compliance requirements, reduce costs and protect your business.  Sumsub has over 2,000 clients in fintech, crypto, transportation, trading, e-commerce and gaming industries including Binance, Wirex, Avis, Bybit, Huobi, Unlimit, Flutter, Kaizen Gaming, and TransferGo.

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from sumsub_python_sdk.paths.resources_applicants_applicant_id_info_company_info_beneficiaries.post import AddBeneficiaryRaw
from sumsub_python_sdk.paths.resources_applicants_applicant_id_agreement.post import AddConsentToProfileRaw
from sumsub_python_sdk.paths.resources_applicants_applicant_id_tags_add.post import AddCustomTagsRaw
from sumsub_python_sdk.paths.resources_applicants_applicant_id_tags.post import AddCustomTags0Raw
from sumsub_python_sdk.paths.resources_applicants_applicant_id_info_id_doc.post import AddIdDocumentRaw
from sumsub_python_sdk.paths.resources_applicant_actions_action_id_images.post import AddImageToPaymentMethodRaw
from sumsub_python_sdk.paths.resources_applicant_actions_action_id_payment_method.post import AddPaymentMethodInformationRaw
from sumsub_python_sdk.paths.resources_applicants_applicant_id_blacklistnotenote.post import AddToBlocklistRaw
from sumsub_python_sdk.paths.resources_applicants_applicant_id_info_company_info.patch import ChangeCompanyDataRaw
from sumsub_python_sdk.paths.resources_applicants_applicant_id_info.patch import ChangeExtractedInfoRaw
from sumsub_python_sdk.paths.resources_applicants_applicant_id_move_to_level.post import ChangeRequiredDocumentSetRaw
from sumsub_python_sdk.paths.resources_moderation_states__applicant_idapplicant_id.get import ClarifyRejectionReasonRaw
from sumsub_python_sdk.paths.resources_applicants_applicant_id_ekyc_confirm_confirmationid.post import ConfirmDataRaw
from sumsub_python_sdk.paths.resources_applicant_actions___for_applicant_applicant_idlevel_namelevel_name.post import CreateActionRaw
from sumsub_python_sdk.paths.resources_applicant_actions___for_applicant_applicant_id_crypto_source_of_funds.post import CreateCryptoSourceOfFundsRaw
from sumsub_python_sdk.paths.resources_applicant_actions___for_applicant_applicant_id_level_namepayment_source.post import CreatePaymentSourceActionsRaw
from sumsub_python_sdk.paths.resources_applicants_applicant_id_presence_status.patch import DeactivateProfileRaw
from sumsub_python_sdk.paths.resources_kyt_txns_txn_id_data_applicant.patch import EnrichTransactionWithTravelRuleDataRaw
from sumsub_python_sdk.paths.resources_applicant_actions_action_id_one.get import GetActionOneInfoRaw
from sumsub_python_sdk.paths.resources_applicant_actions__applicant_idapplicant_id.get import GetActionsRaw
from sumsub_python_sdk.paths.resources_applicant_actions_action_id_images_image_idpreviewis_preview.get import GetBankCardImageRaw
from sumsub_python_sdk.paths.resources_applicants_applicant_id_one.get import GetDataRaw
from sumsub_python_sdk.paths.resources_applicants__external_user_idexternal_user_id_one.get import GetDataByExternalUserIdRaw
from sumsub_python_sdk.paths.resources_checks_latest.get import GetDataLatestRaw
from sumsub_python_sdk.paths.resources_applicant_fraud_networks_network_id_one.get import GetFraudNetworkByIdRaw
from sumsub_python_sdk.paths.resources_applicant_fraud_networks.get import GetFraudNetworksRaw
from sumsub_python_sdk.paths.resources_applicant_fraud_networks___by_applicant_applicant_id.get import GetFraudNetworksByApplicantRaw
from sumsub_python_sdk.paths.resources_applicants___levels.get import GetLevelsRaw
from sumsub_python_sdk.paths.resources_applicants_applicant_id_required_id_docs.post import GetRequiredIdDocsRaw
from sumsub_python_sdk.paths.resources_applicants_applicant_id_status.get import GetReviewStatusRaw
from sumsub_python_sdk.paths.resources_applicants_applicant_id_required_id_docs_status.get import GetVerificationStepsStatusRaw
from sumsub_python_sdk.paths.resources_video_ident_applicant_applicant_id_media_composition_media_id.get import GetVideoCallMediaRaw
from sumsub_python_sdk.paths.resources_applicants___applicant_import.post import ImportByArchiveRaw
from sumsub_python_sdk.paths.resources_applicants___ingest_completedlevel_namelevel_name.post import ImportCompletedRaw
from sumsub_python_sdk.paths.resources_applicants_applicant_id_status_pendingreasonreason.post import InitiateApplicantCheckRaw
from sumsub_python_sdk.paths.resources_kyt_txns_txn_id_applicant_id_applicant_id.post import MoveTransactionToAnotherApplicantRaw
from sumsub_python_sdk.paths.resources_applicants_applicant_id_tags.delete import RemoveCustomTagsRaw
from sumsub_python_sdk.paths.resources_applicants_applicant_id_info_company_info_beneficiaries_beneficiary_applicant_id.delete import RemoveFromBeneficiaryListRaw
from sumsub_python_sdk.paths.resources_applicant_actions_action_id_review_status_pending.post import RequestActionCheckRaw
from sumsub_python_sdk.paths.resources_applicants_applicant_id_reset.post import ResetProfileRaw
from sumsub_python_sdk.paths.resources_applicants_applicant_id_reset_step_id_doc_set_type.post import ResetVerificationStepRaw
from sumsub_python_sdk.paths.resources_applicants_applicant_id_status_test_completed.post import SandboxVerificationResponseRaw
from sumsub_python_sdk.paths.resources_applicants_applicant_id_ekyc_submit.post import SubmitDataNoDocVerificationRaw
from sumsub_python_sdk.paths.resources_applicant_actions___for_applicant_applicant_id_payment_method.post import SubmitPaymentMethodRaw
from sumsub_python_sdk.paths.resources_applicants_applicant_id_kyt_txns___data.post import SubmitTransactionDataRaw
from sumsub_python_sdk.paths.resources_applicants___kyt_txns___data.post import SubmitTransactionForNonExistingRaw
from sumsub_python_sdk.paths.resources_applicants_applicant_id_fixed_info.patch import UpdateFixedInfoRaw
from sumsub_python_sdk.paths.resources_applicants.patch import UpdateTopLevelInfoRaw


class ApplicantApiRaw(
    AddBeneficiaryRaw,
    AddConsentToProfileRaw,
    AddCustomTagsRaw,
    AddCustomTags0Raw,
    AddIdDocumentRaw,
    AddImageToPaymentMethodRaw,
    AddPaymentMethodInformationRaw,
    AddToBlocklistRaw,
    ChangeCompanyDataRaw,
    ChangeExtractedInfoRaw,
    ChangeRequiredDocumentSetRaw,
    ClarifyRejectionReasonRaw,
    ConfirmDataRaw,
    CreateActionRaw,
    CreateCryptoSourceOfFundsRaw,
    CreatePaymentSourceActionsRaw,
    DeactivateProfileRaw,
    EnrichTransactionWithTravelRuleDataRaw,
    GetActionOneInfoRaw,
    GetActionsRaw,
    GetBankCardImageRaw,
    GetDataRaw,
    GetDataByExternalUserIdRaw,
    GetDataLatestRaw,
    GetFraudNetworkByIdRaw,
    GetFraudNetworksRaw,
    GetFraudNetworksByApplicantRaw,
    GetLevelsRaw,
    GetRequiredIdDocsRaw,
    GetReviewStatusRaw,
    GetVerificationStepsStatusRaw,
    GetVideoCallMediaRaw,
    ImportByArchiveRaw,
    ImportCompletedRaw,
    InitiateApplicantCheckRaw,
    MoveTransactionToAnotherApplicantRaw,
    RemoveCustomTagsRaw,
    RemoveFromBeneficiaryListRaw,
    RequestActionCheckRaw,
    ResetProfileRaw,
    ResetVerificationStepRaw,
    SandboxVerificationResponseRaw,
    SubmitDataNoDocVerificationRaw,
    SubmitPaymentMethodRaw,
    SubmitTransactionDataRaw,
    SubmitTransactionForNonExistingRaw,
    UpdateFixedInfoRaw,
    UpdateTopLevelInfoRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
