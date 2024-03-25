<div align="left">

[![Visit Sumsub](./header.png)](https://sumsub.com&#x2F;)

# Sumsub<a id="sumsub"></a>

Sumsub is the one verification platform to secure the whole user journey. With Sumsub's customizable KYC, KYB, transaction monitoring and fraud prevention solutions, you can orchestrate your verification process, welcome more customers worldwide, meet compliance requirements, reduce costs and protect your business.

Sumsub has over 2,000 clients in fintech, crypto, transportation, trading, e-commerce and gaming industries including Binance, Wirex, Avis, Bybit, Huobi, Unlimit, Flutter, Kaizen Gaming, and TransferGo.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`sumsub.analysis.standalone_crypto_initiation`](#sumsubanalysisstandalone_crypto_initiation)
  * [`sumsub.applicant.add_beneficiary`](#sumsubapplicantadd_beneficiary)
  * [`sumsub.applicant.add_consent_to_profile`](#sumsubapplicantadd_consent_to_profile)
  * [`sumsub.applicant.add_custom_tags`](#sumsubapplicantadd_custom_tags)
  * [`sumsub.applicant.add_custom_tags_0`](#sumsubapplicantadd_custom_tags_0)
  * [`sumsub.applicant.add_id_document`](#sumsubapplicantadd_id_document)
  * [`sumsub.applicant.add_image_to_payment_method`](#sumsubapplicantadd_image_to_payment_method)
  * [`sumsub.applicant.add_payment_method_information`](#sumsubapplicantadd_payment_method_information)
  * [`sumsub.applicant.add_to_blocklist`](#sumsubapplicantadd_to_blocklist)
  * [`sumsub.applicant.change_company_data`](#sumsubapplicantchange_company_data)
  * [`sumsub.applicant.change_extracted_info`](#sumsubapplicantchange_extracted_info)
  * [`sumsub.applicant.change_required_document_set`](#sumsubapplicantchange_required_document_set)
  * [`sumsub.applicant.clarify_rejection_reason`](#sumsubapplicantclarify_rejection_reason)
  * [`sumsub.applicant.confirm_data`](#sumsubapplicantconfirm_data)
  * [`sumsub.applicant.create_action`](#sumsubapplicantcreate_action)
  * [`sumsub.applicant.create_crypto_source_of_funds`](#sumsubapplicantcreate_crypto_source_of_funds)
  * [`sumsub.applicant.create_payment_source_actions`](#sumsubapplicantcreate_payment_source_actions)
  * [`sumsub.applicant.deactivate_profile`](#sumsubapplicantdeactivate_profile)
  * [`sumsub.applicant.enrich_transaction_with_travel_rule_data`](#sumsubapplicantenrich_transaction_with_travel_rule_data)
  * [`sumsub.applicant.get_action_one_info`](#sumsubapplicantget_action_one_info)
  * [`sumsub.applicant.get_actions`](#sumsubapplicantget_actions)
  * [`sumsub.applicant.get_bank_card_image`](#sumsubapplicantget_bank_card_image)
  * [`sumsub.applicant.get_data`](#sumsubapplicantget_data)
  * [`sumsub.applicant.get_data_by_external_user_id`](#sumsubapplicantget_data_by_external_user_id)
  * [`sumsub.applicant.get_data_latest`](#sumsubapplicantget_data_latest)
  * [`sumsub.applicant.get_fraud_network_by_id`](#sumsubapplicantget_fraud_network_by_id)
  * [`sumsub.applicant.get_fraud_networks`](#sumsubapplicantget_fraud_networks)
  * [`sumsub.applicant.get_fraud_networks_by_applicant`](#sumsubapplicantget_fraud_networks_by_applicant)
  * [`sumsub.applicant.get_levels`](#sumsubapplicantget_levels)
  * [`sumsub.applicant.get_required_id_docs`](#sumsubapplicantget_required_id_docs)
  * [`sumsub.applicant.get_review_status`](#sumsubapplicantget_review_status)
  * [`sumsub.applicant.get_verification_steps_status`](#sumsubapplicantget_verification_steps_status)
  * [`sumsub.applicant.get_video_call_media`](#sumsubapplicantget_video_call_media)
  * [`sumsub.applicant.import_by_archive`](#sumsubapplicantimport_by_archive)
  * [`sumsub.applicant.import_completed`](#sumsubapplicantimport_completed)
  * [`sumsub.applicant.initiate_applicant_check`](#sumsubapplicantinitiate_applicant_check)
  * [`sumsub.applicant.move_transaction_to_another_applicant`](#sumsubapplicantmove_transaction_to_another_applicant)
  * [`sumsub.applicant.remove_custom_tags`](#sumsubapplicantremove_custom_tags)
  * [`sumsub.applicant.remove_from_beneficiary_list`](#sumsubapplicantremove_from_beneficiary_list)
  * [`sumsub.applicant.request_action_check`](#sumsubapplicantrequest_action_check)
  * [`sumsub.applicant.reset_profile`](#sumsubapplicantreset_profile)
  * [`sumsub.applicant.reset_verification_step`](#sumsubapplicantreset_verification_step)
  * [`sumsub.applicant.sandbox_verification_response`](#sumsubapplicantsandbox_verification_response)
  * [`sumsub.applicant.submit_data_no_doc_verification`](#sumsubapplicantsubmit_data_no_doc_verification)
  * [`sumsub.applicant.submit_payment_method`](#sumsubapplicantsubmit_payment_method)
  * [`sumsub.applicant.submit_transaction_data`](#sumsubapplicantsubmit_transaction_data)
  * [`sumsub.applicant.submit_transaction_for_non_existing`](#sumsubapplicantsubmit_transaction_for_non_existing)
  * [`sumsub.applicant.update_fixed_info`](#sumsubapplicantupdate_fixed_info)
  * [`sumsub.applicant.update_top_level_info`](#sumsubapplicantupdate_top_level_info)
  * [`sumsub.audit_trail_event.get_events`](#sumsubaudit_trail_eventget_events)
  * [`sumsub.check.additional_company_data`](#sumsubcheckadditional_company_data)
  * [`sumsub.check.additional_poa_data`](#sumsubcheckadditional_poa_data)
  * [`sumsub.check.email_confirmation_results`](#sumsubcheckemail_confirmation_results)
  * [`sumsub.check.ip_check_results`](#sumsubcheckip_check_results)
  * [`sumsub.check.perform_name_cross_validation`](#sumsubcheckperform_name_cross_validation)
  * [`sumsub.check.phone_confirmation_results`](#sumsubcheckphone_confirmation_results)
  * [`sumsub.check.tin_ssn_check_results`](#sumsubchecktin_ssn_check_results)
  * [`sumsub.health.status_api_get`](#sumsubhealthstatus_api_get)
  * [`sumsub.image.get_document_images`](#sumsubimageget_document_images)
  * [`sumsub.image.mark_as_inactive`](#sumsubimagemark_as_inactive)
  * [`sumsub.inspection.get_video_ident_data`](#sumsubinspectionget_video_ident_data)
  * [`sumsub.note.add_to_transaction`](#sumsubnoteadd_to_transaction)
  * [`sumsub.note.get_transaction_notes`](#sumsubnoteget_transaction_notes)
  * [`sumsub.note.remove_from_transaction`](#sumsubnoteremove_from_transaction)
  * [`sumsub.note.update_transaction_notes`](#sumsubnoteupdate_transaction_notes)
  * [`sumsub.tag.add_transaction_tags`](#sumsubtagadd_transaction_tags)
  * [`sumsub.token.create_action_token`](#sumsubtokencreate_action_token)
  * [`sumsub.token.get_available_currencies`](#sumsubtokenget_available_currencies)
  * [`sumsub.transaction.approve_reject`](#sumsubtransactionapprove_reject)
  * [`sumsub.transaction.bulk_import`](#sumsubtransactionbulk_import)
  * [`sumsub.transaction.confirm_ownership`](#sumsubtransactionconfirm_ownership)
  * [`sumsub.transaction.get_one_data`](#sumsubtransactionget_one_data)
  * [`sumsub.transaction.information_one`](#sumsubtransactioninformation_one)
  * [`sumsub.transaction.list_tags`](#sumsubtransactionlist_tags)
  * [`sumsub.transaction.re_score`](#sumsubtransactionre_score)
  * [`sumsub.transaction.remove_ownership`](#sumsubtransactionremove_ownership)
  * [`sumsub.transaction.remove_tags`](#sumsubtransactionremove_tags)
  * [`sumsub.transaction.update_blockchain_info`](#sumsubtransactionupdate_blockchain_info)
  * [`sumsub.transaction.update_properties`](#sumsubtransactionupdate_properties)
  * [`sumsub.vasp.get_available_vasps`](#sumsubvaspget_available_vasps)
  * [`sumsub.web_sdk_link.generate_external`](#sumsubweb_sdk_linkgenerate_external)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Sumsub&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from sumsub_python_sdk import Sumsub, ApiException

sumsub = Sumsub(

        sec0 = 'YOUR_API_KEY',
)

try:
    # Standalone crypto analysis
    sumsub.analysis.standalone_crypto_initiation(
        currency="string_example",
        direction="string_example",
        address="string_example",
        txn="string_example",
        token_id="string_example",
    )
except ApiException as e:
    print("Exception when calling AnalysisApi.standalone_crypto_initiation: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from sumsub_python_sdk import Sumsub, ApiException

sumsub = Sumsub(

        sec0 = 'YOUR_API_KEY',
)

async def main():
    try:
        # Standalone crypto analysis
        await sumsub.analysis.astandalone_crypto_initiation(
            currency="string_example",
            direction="string_example",
            address="string_example",
            txn="string_example",
            token_id="string_example",
        )
    except ApiException as e:
        print("Exception when calling AnalysisApi.standalone_crypto_initiation: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from sumsub_python_sdk import Sumsub, ApiException

sumsub = Sumsub(

        sec0 = 'YOUR_API_KEY',
)

try:
    # Standalone crypto analysis
    standalone_crypto_initiation_response = sumsub.analysis.raw.standalone_crypto_initiation(
        currency="string_example",
        direction="string_example",
        address="string_example",
        txn="string_example",
        token_id="string_example",
    )
    pprint(standalone_crypto_initiation_response.headers)
    pprint(standalone_crypto_initiation_response.status)
    pprint(standalone_crypto_initiation_response.round_trip_time)
except ApiException as e:
    print("Exception when calling AnalysisApi.standalone_crypto_initiation: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `sumsub.analysis.standalone_crypto_initiation`<a id="sumsubanalysisstandalone_crypto_initiation"></a>

Initiates standalone crypto analysis.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.analysis.standalone_crypto_initiation(
    currency="string_example",
    direction="string_example",
    address="string_example",
    txn="string_example",
    token_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### currency: `str`<a id="currency-str"></a>

`BTC`, `ETH`, `BCH`, `LTC`, `USDT`, `ERC-20`, `BSV`, `XLM`, ...

##### direction: `str`<a id="direction-str"></a>

An operation type. Can be `withdrawal` or `deposit`.

##### address: `str`<a id="address-str"></a>

Target address hash.

##### txn: `str`<a id="txn-str"></a>

Transaction hash. For `withdrawals`, `txn` should not be set at all or set to `null`.

##### token_id: `str`<a id="token_id-str"></a>

Check the [Get available tokens](ref:get-available-tokens) method to get the full list of available currencies and token IDs.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AnalysisStandaloneCryptoInitiationRequest`](./sumsub_python_sdk/type/analysis_standalone_crypto_initiation_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/standalone/crypto/cryptoSourceOfFunds` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.applicant.add_beneficiary`<a id="sumsubapplicantadd_beneficiary"></a>

Adds an existing individual applicant as a beneficiary.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.applicant.add_beneficiary(
    applicant={
    },
    applicant_id="string_example",
    type="string_example",
    applicant_id="applicantId_example",
    positions=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### applicant_id: `str`<a id="applicant_id-str"></a>

A unique company applicant identifier.

##### requestBody: [`ApplicantAddBeneficiaryRequest`](./sumsub_python_sdk/type/applicant_add_beneficiary_request.py)<a id="requestbody-applicantaddbeneficiaryrequestsumsub_python_sdktypeapplicant_add_beneficiary_requestpy"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/applicants/{applicantId}/info/companyInfo/beneficiaries` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.applicant.add_consent_to_profile`<a id="sumsubapplicantadd_consent_to_profile"></a>

Adds a consent to an applicant profile.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.applicant.add_consent_to_profile(
    records=[
        {
        }
    ],
    applicant_id="applicantId_example",
    accepted_at="string_example",
    residence_country="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### records: [`ApplicantAddConsentToProfileRequestRecords`](./sumsub_python_sdk/type/applicant_add_consent_to_profile_request_records.py)<a id="records-applicantaddconsenttoprofilerequestrecordssumsub_python_sdktypeapplicant_add_consent_to_profile_request_recordspy"></a>

##### applicant_id: `str`<a id="applicant_id-str"></a>

A unique identifier of an applicant profile to which a consent should be added.

##### accepted_at: `str`<a id="accepted_at-str"></a>

Date and time a consent was accepted by the applicant.

##### residence_country: `str`<a id="residence_country-str"></a>

An applicant country of residence.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ApplicantAddConsentToProfileRequest`](./sumsub_python_sdk/type/applicant_add_consent_to_profile_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/applicants/{applicantId}/agreement` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.applicant.add_custom_tags`<a id="sumsubapplicantadd_custom_tags"></a>

Adds custom tags to applicant profiles.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.applicant.add_custom_tags(
    applicant_id="applicantId_example",
    raw_body=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### applicant_id: `str`<a id="applicant_id-str"></a>

A unique applicant identifier.

##### raw_body: [`ApplicantAddCustomTagsRequestRawBody`](./sumsub_python_sdk/type/applicant_add_custom_tags_request_raw_body.py)<a id="raw_body-applicantaddcustomtagsrequestrawbodysumsub_python_sdktypeapplicant_add_custom_tags_request_raw_bodypy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ApplicantAddCustomTagsRequest`](./sumsub_python_sdk/type/applicant_add_custom_tags_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/applicants/{applicantId}/tags/add` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.applicant.add_custom_tags_0`<a id="sumsubapplicantadd_custom_tags_0"></a>

Adds and overwrites custom tags in applicant profiles.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.applicant.add_custom_tags_0(
    applicant_id="applicantId_example",
    raw_body=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### applicant_id: `str`<a id="applicant_id-str"></a>

A unique applicant identifier.

##### raw_body: [`ApplicantAddCustomTagsRequest2RawBody`](./sumsub_python_sdk/type/applicant_add_custom_tags_request2_raw_body.py)<a id="raw_body-applicantaddcustomtagsrequest2rawbodysumsub_python_sdktypeapplicant_add_custom_tags_request2_raw_bodypy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ApplicantAddCustomTagsRequest2`](./sumsub_python_sdk/type/applicant_add_custom_tags_request2.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/applicants/{applicantId}/tags` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.applicant.add_id_document`<a id="sumsubapplicantadd_id_document"></a>

Adds an identification document to be verified.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_id_document_response = sumsub.applicant.add_id_document(
    x_return_doc_warnings=True,
    applicant_id="applicantId_example",
    metadata={
        "id_doc_type": "id_doc_type_example",
        "country": "country_example",
    },
    content=open('/path/to/file', 'rb'),
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### x_return_doc_warnings: `bool`<a id="x_return_doc_warnings-bool"></a>

`true` / `false`

##### applicant_id: `str`<a id="applicant_id-str"></a>

A unique applicant identifier.

##### metadata: [`ApplicantAddIdDocumentRequestMetadata`](./sumsub_python_sdk/type/applicant_add_id_document_request_metadata.py)<a id="metadata-applicantaddiddocumentrequestmetadatasumsub_python_sdktypeapplicant_add_id_document_request_metadatapy"></a>


##### content: `IO`<a id="content-io"></a>

A photo of the document.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ApplicantAddIdDocumentRequest`](./sumsub_python_sdk/type/applicant_add_id_document_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ApplicantAddIdDocumentResponse`](./sumsub_python_sdk/pydantic/applicant_add_id_document_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/applicants/{applicantId}/info/idDoc` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.applicant.add_image_to_payment_method`<a id="sumsubapplicantadd_image_to_payment_method"></a>

Adds an image to the payment method.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.applicant.add_image_to_payment_method(
    content=open('/path/to/file', 'rb'),
    metadata={
        "id_doc_type": "id_doc_type_example",
        "country": "country_example",
    },
    action_id="actionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### content: `IO`<a id="content-io"></a>

A document photo.

##### metadata: [`ApplicantAddImageToPaymentMethodRequestMetadata`](./sumsub_python_sdk/type/applicant_add_image_to_payment_method_request_metadata.py)<a id="metadata-applicantaddimagetopaymentmethodrequestmetadatasumsub_python_sdktypeapplicant_add_image_to_payment_method_request_metadatapy"></a>


##### action_id: `str`<a id="action_id-str"></a>

A unique applicant action identifier.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ApplicantAddImageToPaymentMethodRequest`](./sumsub_python_sdk/type/applicant_add_image_to_payment_method_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/applicantActions/{actionId}/images` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.applicant.add_payment_method_information`<a id="sumsubapplicantadd_payment_method_information"></a>

Adds additional information to the payment method.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.applicant.add_payment_method_information(
    type="string_example",
    action_id="actionId_example",
    sub_type="string_example",
    data={
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: `str`<a id="type-str"></a>

A payment type. Can be: `bankCard`, `eWallet`, `wireTransfer`.

##### action_id: `str`<a id="action_id-str"></a>

A unique applicant action identifier.

##### sub_type: `str`<a id="sub_type-str"></a>

A payment subtype. For example, `VISA`, `MASTERCARD`, etc.

##### data: [`ApplicantAddPaymentMethodInformationRequestData`](./sumsub_python_sdk/type/applicant_add_payment_method_information_request_data.py)<a id="data-applicantaddpaymentmethodinformationrequestdatasumsub_python_sdktypeapplicant_add_payment_method_information_request_datapy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ApplicantAddPaymentMethodInformationRequest`](./sumsub_python_sdk/type/applicant_add_payment_method_information_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/applicantActions/{actionId}/paymentMethod` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.applicant.add_to_blocklist`<a id="sumsubapplicantadd_to_blocklist"></a>

Add an applicant to blocklist.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.applicant.add_to_blocklist(
    note="note_example",
    applicant_id="applicantId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### note: `str`<a id="note-str"></a>

A note indicating the reason for blocklisting the applicant profile.

##### applicant_id: `str`<a id="applicant_id-str"></a>

A unique applicant identifier.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/applicants/{applicantId}/blacklist?note&#x3D;{note}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.applicant.change_company_data`<a id="sumsubapplicantchange_company_data"></a>

Changes company data.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.applicant.change_company_data(
    company_name="string_example",
    registration_number="string_example",
    applicant_id="applicantId_example",
    country="string_example",
    legal_address="string_example",
    incorporated_on="string_example",
    type="string_example",
    email="string_example",
    control_scheme="string_example",
    phone="string_example",
    tax_id="string_example",
    registration_location="string_example",
    website="string_example",
    postal_address="string_example",
    beneficiaries=[
        "string_example"
    ],
    addresses=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_name: `str`<a id="company_name-str"></a>

Name of the company.

##### registration_number: `str`<a id="registration_number-str"></a>

Registration number.

##### applicant_id: `str`<a id="applicant_id-str"></a>

A unique applicant identifier.

##### country: `str`<a id="country-str"></a>

A three-letter country code (e.g. `DEU`).

##### legal_address: `str`<a id="legal_address-str"></a>

Legal name.

##### incorporated_on: `str`<a id="incorporated_on-str"></a>

Date of incorporation (format `YYYY-mm-dd`, e.g. 2001-09-25).

##### type: `str`<a id="type-str"></a>

Type of entity.

##### email: `str`<a id="email-str"></a>

Email address.

##### control_scheme: `str`<a id="control_scheme-str"></a>

Description of the control scheme of the group of entities.

##### phone: `str`<a id="phone-str"></a>

Phone number.

##### tax_id: `str`<a id="tax_id-str"></a>

Taxpayer registration number/Code of taxpayer registration.

##### registration_location: `str`<a id="registration_location-str"></a>

Location of registration.

##### website: `str`<a id="website-str"></a>

Website's URL.

##### postal_address: `str`<a id="postal_address-str"></a>

Postal address.

##### beneficiaries: [`ApplicantChangeCompanyDataRequestBeneficiaries`](./sumsub_python_sdk/type/applicant_change_company_data_request_beneficiaries.py)<a id="beneficiaries-applicantchangecompanydatarequestbeneficiariessumsub_python_sdktypeapplicant_change_company_data_request_beneficiariespy"></a>

##### addresses: [`ApplicantChangeCompanyDataRequestAddresses`](./sumsub_python_sdk/type/applicant_change_company_data_request_addresses.py)<a id="addresses-applicantchangecompanydatarequestaddressessumsub_python_sdktypeapplicant_change_company_data_request_addressespy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ApplicantChangeCompanyDataRequest`](./sumsub_python_sdk/type/applicant_change_company_data_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/applicants/{applicantId}/info/companyInfo` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.applicant.change_extracted_info`<a id="sumsubapplicantchange_extracted_info"></a>

Changes extracted information.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.applicant.change_extracted_info(
    applicant_id="applicantId_example",
    first_name="string_example",
    last_name="string_example",
    middle_name="string_example",
    legal_name="string_example",
    gender="string_example",
    dob="string_example",
    place_of_birth="string_example",
    country_of_birth="string_example",
    state_of_birth="string_example",
    country="string_example",
    nationality="string_example",
    addresses="string_example",
    tin="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### applicant_id: `str`<a id="applicant_id-str"></a>

A unique applicant identifier.

##### first_name: `str`<a id="first_name-str"></a>

The first name of the applicant.

##### last_name: `str`<a id="last_name-str"></a>

The last name of the applicant.

##### middle_name: `str`<a id="middle_name-str"></a>

The middle name of the applicant.

##### legal_name: `str`<a id="legal_name-str"></a>

Legal name.

##### gender: `str`<a id="gender-str"></a>

An applicant gender (`M` or `F`).

##### dob: `str`<a id="dob-str"></a>

Applicant date of birth (format `YYYY-mm-dd`, e.g. 2001-09-25).

##### place_of_birth: `str`<a id="place_of_birth-str"></a>

The applicant birthplace.

##### country_of_birth: `str`<a id="country_of_birth-str"></a>

Applicant country of birth.

##### state_of_birth: `str`<a id="state_of_birth-str"></a>

Applicant state of birth.

##### country: `str`<a id="country-str"></a>

Alpha-3 country code (e.g. `DEU` or `GBR`).

##### nationality: `str`<a id="nationality-str"></a>

Alpha-3 country code.

##### addresses: `str`<a id="addresses-str"></a>

List of applicant addresses.

##### tin: `str`<a id="tin-str"></a>

Tax identification number.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ApplicantChangeExtractedInfoRequest`](./sumsub_python_sdk/type/applicant_change_extracted_info_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/applicants/{applicantId}/info` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.applicant.change_required_document_set`<a id="sumsubapplicantchange_required_document_set"></a>

Changes the list of required documents.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.applicant.change_required_document_set(
    name="name_example",
    applicant_id="applicantId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

A [verification level](https://docs.sumsub.com/reference) name. Case-sensitive and has to be created in the same environment. If contains reserved characters (e.g., `@`, `+\"`, white spaces as `%20`), it should be URL-encoded, otherwise you may get signature mismatch.

##### applicant_id: `str`<a id="applicant_id-str"></a>

A unique applicant identifier.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/applicants/{applicantId}/moveToLevel` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.applicant.clarify_rejection_reason`<a id="sumsubapplicantclarify_rejection_reason"></a>

Returns rejection reason clarification.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.applicant.clarify_rejection_reason(
    applicant_id="applicantId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### applicant_id: `str`<a id="applicant_id-str"></a>

A unique applicant identifier.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/moderationStates/-;applicantId&#x3D;{applicantId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.applicant.confirm_data`<a id="sumsubapplicantconfirm_data"></a>

Confirms applicant data.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.applicant.confirm_data(
    applicant_id="applicantId_example",
    confirmation_id="confirmationId_example",
    otp={
        "code": "code_example",
    },
    oauth={
        "complete_url": "complete_url_example",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### applicant_id: `str`<a id="applicant_id-str"></a>

A unique applicant identifier.

##### confirmation_id: `str`<a id="confirmation_id-str"></a>

A confirmation identifier from the [submission](ref:submit-applicant-data) response.

##### otp: [`ApplicantConfirmDataRequestOtp`](./sumsub_python_sdk/type/applicant_confirm_data_request_otp.py)<a id="otp-applicantconfirmdatarequestotpsumsub_python_sdktypeapplicant_confirm_data_request_otppy"></a>


##### oauth: [`ApplicantConfirmDataRequestOauth`](./sumsub_python_sdk/type/applicant_confirm_data_request_oauth.py)<a id="oauth-applicantconfirmdatarequestoauthsumsub_python_sdktypeapplicant_confirm_data_request_oauthpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ApplicantConfirmDataRequest`](./sumsub_python_sdk/type/applicant_confirm_data_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/applicants/{applicantId}/ekyc/confirm/{confirmationid}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.applicant.create_action`<a id="sumsubapplicantcreate_action"></a>

Creates an applicant action.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.applicant.create_action(
    external_action_id="string_example",
    applicant_id="applicantId_example",
    level_name="levelName_example",
    payment_method={
        "type": "type_example",
    },
    email="string_example",
    phone="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### external_action_id: `str`<a id="external_action_id-str"></a>

An external action ID which will be bound to the token.

##### applicant_id: `str`<a id="applicant_id-str"></a>

A unique aplicant identifier.

##### level_name: `str`<a id="level_name-str"></a>

A name of the level configured in the dashboard.

##### payment_method: [`ApplicantCreateActionRequestPaymentMethod`](./sumsub_python_sdk/type/applicant_create_action_request_payment_method.py)<a id="payment_method-applicantcreateactionrequestpaymentmethodsumsub_python_sdktypeapplicant_create_action_request_payment_methodpy"></a>


##### email: `str`<a id="email-str"></a>

Applicant email address.

##### phone: `str`<a id="phone-str"></a>

Applicant phone number.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ApplicantCreateActionRequest`](./sumsub_python_sdk/type/applicant_create_action_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/applicantActions/-/forApplicant/{applicantId}?levelName&#x3D;{levelName}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.applicant.create_crypto_source_of_funds`<a id="sumsubapplicantcreate_crypto_source_of_funds"></a>

Creates an action with transaction information.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.applicant.create_crypto_source_of_funds(
    currency="string_example",
    direction="string_example",
    address="string_example",
    applicant_id="applicantId_example",
    txn="string_example",
    token_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### currency: `str`<a id="currency-str"></a>

`BTC`, `ETH`, `BCH`, `LTC`, `USDT`, `ERC-20`, `BSV`, `XLM`, ...

##### direction: `str`<a id="direction-str"></a>

Operation type. Can be `withdrawal` or `deposit`.

##### address: `str`<a id="address-str"></a>

Target address hash.

##### applicant_id: `str`<a id="applicant_id-str"></a>

A unique applicant identifier.

##### txn: `str`<a id="txn-str"></a>

Transaction hash. For `withdrawals`, `txn` should not be set at all or set to `null`.

##### token_id: `str`<a id="token_id-str"></a>

Check the [Get available tokens](ref:get-available-tokens) method to get the full list of available currencies and token IDs.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ApplicantCreateCryptoSourceOfFundsRequest`](./sumsub_python_sdk/type/applicant_create_crypto_source_of_funds_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/applicantActions/-/forApplicant/{applicantId}/cryptoSourceOfFunds` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.applicant.create_payment_source_actions`<a id="sumsubapplicantcreate_payment_source_actions"></a>

Creates an action to process a payment source and to confirm the owner of the payment method.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_payment_source_actions_response = sumsub.applicant.create_payment_source_actions(
    applicant_id="applicantId_example",
    level_name="levelName_example",
    external_action_id="string_example",
    payment_source={
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### applicant_id: `str`<a id="applicant_id-str"></a>

An unique applicant identifier.

##### level_name: `str`<a id="level_name-str"></a>

A verification level name for which you want to create a payment source action.

##### external_action_id: `str`<a id="external_action_id-str"></a>

An external identifier for an action.

##### payment_source: [`ApplicantCreatePaymentSourceActionsRequestPaymentSource`](./sumsub_python_sdk/type/applicant_create_payment_source_actions_request_payment_source.py)<a id="payment_source-applicantcreatepaymentsourceactionsrequestpaymentsourcesumsub_python_sdktypeapplicant_create_payment_source_actions_request_payment_sourcepy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ApplicantCreatePaymentSourceActionsRequest`](./sumsub_python_sdk/type/applicant_create_payment_source_actions_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ApplicantCreatePaymentSourceActionsResponse`](./sumsub_python_sdk/pydantic/applicant_create_payment_source_actions_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/applicantActions/-/forApplicant/{applicantId}/?levelName&#x3D;paymentSource` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.applicant.deactivate_profile`<a id="sumsubapplicantdeactivate_profile"></a>

Deactivates an applicant profile.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.applicant.deactivate_profile(
    applicant_id="applicantId_example",
    status="status_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### applicant_id: `str`<a id="applicant_id-str"></a>

A unique applicant identifier.

##### status: `str`<a id="status-str"></a>

Possible values: `deactivated` to deactivate the applicant profile. `activated` to reactivate the applicant profile.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/applicants/{applicantId}/presence/{status}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.applicant.enrich_transaction_with_travel_rule_data`<a id="sumsubapplicantenrich_transaction_with_travel_rule_data"></a>

Enriches transaction with the Travel Rule data.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
enrich_transaction_with_travel_rule_data_response = sumsub.applicant.enrich_transaction_with_travel_rule_data(
    full_name="string_example",
    txn_id="txnId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### full_name: `str`<a id="full_name-str"></a>

Participant full name.

##### txn_id: `str`<a id="txn_id-str"></a>

A unique transaction identifier.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ApplicantEnrichTransactionWithTravelRuleDataRequest`](./sumsub_python_sdk/type/applicant_enrich_transaction_with_travel_rule_data_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/kyt/txns/{txnId}/data/applicant` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.applicant.get_action_one_info`<a id="sumsubapplicantget_action_one_info"></a>

Returns information about the applicant action checks.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.applicant.get_action_one_info(
    action_id="actionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### action_id: `str`<a id="action_id-str"></a>

A unique applicant action identifier.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/applicantActions/{actionId}/one` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.applicant.get_actions`<a id="sumsubapplicantget_actions"></a>

Returns a list of applicant actions.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.applicant.get_actions(
    applicant_id="applicantId_example",
    limit=1000,
    offset=0,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### applicant_id: `str`<a id="applicant_id-str"></a>

A unique applicant identifier.

##### limit: `int`<a id="limit-int"></a>

Limit of applicant actions to be returned.

##### offset: `int`<a id="offset-int"></a>

Offset of applicant actions to be returned.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/applicantActions/-;applicantId&#x3D;{applicantId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.applicant.get_bank_card_image`<a id="sumsubapplicantget_bank_card_image"></a>

Returns an original bank card image.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.applicant.get_bank_card_image(
    action_id="actionId_example",
    image_id="imageId_example",
    is_preview=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### action_id: `str`<a id="action_id-str"></a>

A unique applicant action identifier.

##### image_id: `str`<a id="image_id-str"></a>

An image identifier taken from `images[].imageId`.

##### is_preview: `bool`<a id="is_preview-bool"></a>

Indicates if an image thumbnail should be returned.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/applicantActions/{actionId}/images/{imageId}?preview&#x3D;{isPreview}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.applicant.get_data`<a id="sumsubapplicantget_data"></a>

Returns applicant information.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.applicant.get_data(
    applicant_id="applicantId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### applicant_id: `str`<a id="applicant_id-str"></a>

A unique applicant identifier

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/applicants/{applicantId}/one` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.applicant.get_data_by_external_user_id`<a id="sumsubapplicantget_data_by_external_user_id"></a>

Returns applicant information based on the provided `externalUserId`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.applicant.get_data_by_external_user_id(
    external_user_id="externalUserId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### external_user_id: `str`<a id="external_user_id-str"></a>

A unique applicant identifier in your system.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/applicants/-;externalUserId&#x3D;{externalUserId}/one` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.applicant.get_data_latest`<a id="sumsubapplicantget_data_latest"></a>

Returns the applicant data for Non-Doc verification.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.applicant.get_data_latest(
    type="E_KYC_CHECK",
    applicant_id="applicantId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: `str`<a id="type-str"></a>

Check type.

##### applicant_id: `str`<a id="applicant_id-str"></a>

A unique applicant identifier.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/checks/latest` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.applicant.get_fraud_network_by_id`<a id="sumsubapplicantget_fraud_network_by_id"></a>

Returns fraud network by `networkId`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.applicant.get_fraud_network_by_id(
    network_id="networkId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### network_id: `str`<a id="network_id-str"></a>

A unique network identifier.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/applicantFraudNetworks/{networkId}/one` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.applicant.get_fraud_networks`<a id="sumsubapplicantget_fraud_networks"></a>

Returns fraud networks.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.applicant.get_fraud_networks(
    offset=0,
    limit=10,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### offset: `int`<a id="offset-int"></a>

Offset of the found networks to be returned.

##### limit: `int`<a id="limit-int"></a>

Maximum number of the found networks to be returned. The maximum value you can set is 100.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/applicantFraudNetworks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.applicant.get_fraud_networks_by_applicant`<a id="sumsubapplicantget_fraud_networks_by_applicant"></a>

Returns all fraud networks by `applicantId`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.applicant.get_fraud_networks_by_applicant(
    applicant_id="applicantId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### applicant_id: `str`<a id="applicant_id-str"></a>

A unique applicant identifier.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/applicantFraudNetworks/-/byApplicant/{applicantId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.applicant.get_levels`<a id="sumsubapplicantget_levels"></a>

Returns a list of verification levels.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.applicant.get_levels()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/applicants/-/levels` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.applicant.get_required_id_docs`<a id="sumsubapplicantget_required_id_docs"></a>

Returns the list of required documents.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.applicant.get_required_id_docs(
    applicant_id="applicantId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### applicant_id: `str`<a id="applicant_id-str"></a>

A unique applicant identifier.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/applicants/{applicantId}/requiredIdDocs` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.applicant.get_review_status`<a id="sumsubapplicantget_review_status"></a>

Returns applicant review status.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.applicant.get_review_status(
    applicant_id="applicantId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### applicant_id: `str`<a id="applicant_id-str"></a>

A unique applicant identifier.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/applicants/{applicantId}/status` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.applicant.get_verification_steps_status`<a id="sumsubapplicantget_verification_steps_status"></a>

Returns information about the documents or separate verification step results.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.applicant.get_verification_steps_status(
    applicant_id="applicantId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### applicant_id: `str`<a id="applicant_id-str"></a>

A unique applicant identifier.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/applicants/{applicantId}/requiredIdDocsStatus` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.applicant.get_video_call_media`<a id="sumsubapplicantget_video_call_media"></a>

Returns video call media.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_video_call_media_response = sumsub.applicant.get_video_call_media(
    applicant_id="applicantId_example",
    composition_media_id="compositionMediaId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### applicant_id: `str`<a id="applicant_id-str"></a>

A unique applicant identifier.

##### composition_media_id: `str`<a id="composition_media_id-str"></a>

Video call media identifier.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/videoIdent/applicant/{applicantId}/media/{compositionMediaId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.applicant.import_by_archive`<a id="sumsubapplicantimport_by_archive"></a>

Imports applicant data and images including associated review results.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.applicant.import_by_archive(
    content=open('/path/to/file', 'rb'),
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### content: `IO`<a id="content-io"></a>

An archive file.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ApplicantImportByArchiveRequest`](./sumsub_python_sdk/type/applicant_import_by_archive_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/applicants/-/applicantImport` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.applicant.import_completed`<a id="sumsubapplicantimport_completed"></a>

Imports applicants.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.applicant.import_completed(
    info={
    },
    external_user_id="string_example",
    review={
    },
    level_name="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### info: [`ApplicantImportCompletedRequestInfo`](./sumsub_python_sdk/type/applicant_import_completed_request_info.py)<a id="info-applicantimportcompletedrequestinfosumsub_python_sdktypeapplicant_import_completed_request_infopy"></a>


##### external_user_id: `str`<a id="external_user_id-str"></a>

someClientUserId

##### review: [`ApplicantImportCompletedRequestReview`](./sumsub_python_sdk/type/applicant_import_completed_request_review.py)<a id="review-applicantimportcompletedrequestreviewsumsub_python_sdktypeapplicant_import_completed_request_reviewpy"></a>


##### level_name: `str`<a id="level_name-str"></a>

A [verification level](https://docs.sumsub.com/reference) name. Case-sensitive and has to be created in the same environment. If contains reserved characters (e.g., `@`, `+\"`, white spaces as `%20`), it should be URL-encoded, otherwise you may get signature mismatch.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ApplicantImportCompletedRequest`](./sumsub_python_sdk/type/applicant_import_completed_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/applicants/-/ingestCompleted?levelName&#x3D;{levelName}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.applicant.initiate_applicant_check`<a id="sumsubapplicantinitiate_applicant_check"></a>

Initiates a check of the applicant profile.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.applicant.initiate_applicant_check(
    applicant_id="applicantId_example",
    reason="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### applicant_id: `str`<a id="applicant_id-str"></a>

A unique applicant identifier.

##### reason: `str`<a id="reason-str"></a>

A note indicating the reason for checking the applicant profile.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/applicants/{applicantId}/status/pending?reason&#x3D;{reason}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.applicant.move_transaction_to_another_applicant`<a id="sumsubapplicantmove_transaction_to_another_applicant"></a>

Moves transaction to the specified applicant.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
move_transaction_to_another_applicant_response = sumsub.applicant.move_transaction_to_another_applicant(
    txn_id="txnId_example",
    applicant_id="applicantId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### txn_id: `str`<a id="txn_id-str"></a>

A unique transaction identifier.

##### applicant_id: `str`<a id="applicant_id-str"></a>

A unique applicant identifier who should own the transaction.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/kyt/txns/{txnId}/applicantId/{applicantId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.applicant.remove_custom_tags`<a id="sumsubapplicantremove_custom_tags"></a>

Removes all custom tags from applicant profiles.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.applicant.remove_custom_tags(
    applicant_id="applicantId_example",
    raw_body=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### applicant_id: `str`<a id="applicant_id-str"></a>

A unique applicant identifier.

##### raw_body: [`ApplicantRemoveCustomTagsRequestRawBody`](./sumsub_python_sdk/type/applicant_remove_custom_tags_request_raw_body.py)<a id="raw_body-applicantremovecustomtagsrequestrawbodysumsub_python_sdktypeapplicant_remove_custom_tags_request_raw_bodypy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ApplicantRemoveCustomTagsRequest`](./sumsub_python_sdk/type/applicant_remove_custom_tags_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/applicants/{applicantId}/tags` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.applicant.remove_from_beneficiary_list`<a id="sumsubapplicantremove_from_beneficiary_list"></a>

Removes the applicant from the list of company beneficial owners.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.applicant.remove_from_beneficiary_list(
    applicant_id="applicantId_example",
    beneficiary_applicant_id="beneficiaryApplicantId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### applicant_id: `str`<a id="applicant_id-str"></a>

A unique company applicant identifier.

##### beneficiary_applicant_id: `str`<a id="beneficiary_applicant_id-str"></a>

Beneficiary applicant identifier.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/applicants/{applicantId}/info/companyInfo/beneficiaries/{beneficiaryApplicantId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.applicant.request_action_check`<a id="sumsubapplicantrequest_action_check"></a>

Requests an applicant action check.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.applicant.request_action_check(
    action_id="actionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### action_id: `str`<a id="action_id-str"></a>

A unique applicant action identifier.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/applicantActions/{actionId}/review/status/pending` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.applicant.reset_profile`<a id="sumsubapplicantreset_profile"></a>

Marks documents uploaded by the applicant as inactive and deletes all statuses assigned earlier.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.applicant.reset_profile(
    applicant_id="applicantId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### applicant_id: `str`<a id="applicant_id-str"></a>

A unique applicant identifier.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/applicants/{applicantId}/reset` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.applicant.reset_verification_step`<a id="sumsubapplicantreset_verification_step"></a>

Resets the specified verification step.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.applicant.reset_verification_step(
    applicant_id="applicantId_example",
    id_doc_set_type="idDocSetType_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### applicant_id: `str`<a id="applicant_id-str"></a>

A unique applicant identifier.

##### id_doc_set_type: `str`<a id="id_doc_set_type-str"></a>

A [step name](ref:reset-single-verification-step#available-steps-to-reset) to reset.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/applicants/{applicantId}/resetStep/{idDocSetType}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.applicant.sandbox_verification_response`<a id="sumsubapplicantsandbox_verification_response"></a>

Simulates a verification reposnose.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.applicant.sandbox_verification_response(
    review_answer="string_example",
    reject_labels=[
        "string_example"
    ],
    applicant_id="applicantId_example",
    review_reject_type="string_example",
    client_comment="string_example",
    moderation_comment="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### review_answer: `str`<a id="review_answer-str"></a>

A `GREEN` or `RED` label under which you want to simulate the response. For more information, see [this article](https://docs.sumsub.com/reference).

##### reject_labels: [`ApplicantSandboxVerificationResponseRequestRejectLabels`](./sumsub_python_sdk/type/applicant_sandbox_verification_response_request_reject_labels.py)<a id="reject_labels-applicantsandboxverificationresponserequestrejectlabelssumsub_python_sdktypeapplicant_sandbox_verification_response_request_reject_labelspy"></a>

##### applicant_id: `str`<a id="applicant_id-str"></a>

A unique applicant identifier.

##### review_reject_type: `str`<a id="review_reject_type-str"></a>

A `FINAL` or `RETRY` rejection type indicating whether a rejection should be final or temporary.

##### client_comment: `str`<a id="client_comment-str"></a>

A rejection comment that should not be available to your applicants.

##### moderation_comment: `str`<a id="moderation_comment-str"></a>

A comment that supposed to be shown to the applicant, explaining the reason of rejection.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ApplicantSandboxVerificationResponseRequest`](./sumsub_python_sdk/type/applicant_sandbox_verification_response_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/applicants/{applicantId}/status/testCompleted` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.applicant.submit_data_no_doc_verification`<a id="sumsubapplicantsubmit_data_no_doc_verification"></a>

Sends applicant data for no-document verification.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.applicant.submit_data_no_doc_verification(
    info={
        "country": "country_example",
        "tin": "tin_example",
    },
    applicant_id="applicantId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### info: [`ApplicantSubmitDataNoDocVerificationRequestInfo`](./sumsub_python_sdk/type/applicant_submit_data_no_doc_verification_request_info.py)<a id="info-applicantsubmitdatanodocverificationrequestinfosumsub_python_sdktypeapplicant_submit_data_no_doc_verification_request_infopy"></a>


##### applicant_id: `str`<a id="applicant_id-str"></a>

A unique applicant identifier.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ApplicantSubmitDataNoDocVerificationRequest`](./sumsub_python_sdk/type/applicant_submit_data_no_doc_verification_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/applicants/{applicantId}/ekyc/submit` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.applicant.submit_payment_method`<a id="sumsubapplicantsubmit_payment_method"></a>

Submits a payment method.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.applicant.submit_payment_method(
    x_external_action_id="X-External-Action-Id_example",
    applicant_id="applicantId_example",
    require_selfie=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### x_external_action_id: `str`<a id="x_external_action_id-str"></a>

Use `externalActionId` if you intend to [initialize SDK](ref:about-applicant-actions) for that particular action.

##### applicant_id: `str`<a id="applicant_id-str"></a>

A unique applicant identifier.

##### require_selfie: `bool`<a id="require_selfie-bool"></a>

Sets the video selfie at `requiredIdDocs` for the action.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/applicantActions/-/forApplicant/{applicantId}/paymentMethod` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.applicant.submit_transaction_data`<a id="sumsubapplicantsubmit_transaction_data"></a>

Initiates transaction processing.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.applicant.submit_transaction_data(
    info={
        "direction": "direction_example",
        "amount": 3.14,
        "currency_code": "currency_code_example",
    },
    txn_id="string_example",
    applicant={
        "external_user_id": "external_user_id_example",
        "full_name": "full_name_example",
        "type": "individual",
    },
    counterparty={
        "external_user_id": "external_user_id_example",
        "full_name": "full_name_example",
        "type": "individual",
    },
    applicant_id="applicantId_example",
    txn_date="1970-01-01",
    type="finance",
    source_key="string_example",
    props={
        "custom_txn_limit": "1000",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### info: [`ApplicantSubmitTransactionDataRequestInfo`](./sumsub_python_sdk/type/applicant_submit_transaction_data_request_info.py)<a id="info-applicantsubmittransactiondatarequestinfosumsub_python_sdktypeapplicant_submit_transaction_data_request_infopy"></a>


##### txn_id: `str`<a id="txn_id-str"></a>

A unique transaction identification number. <br>**Note:** If the specified `txnId` already exists, a `409` error code \\\"Entity already exists\\\" is returned. To update an existing transaction, use the [bulk import method](doc:update-transactions-via-bulk-import-method).

##### applicant: [`ApplicantSubmitTransactionDataRequestApplicant`](./sumsub_python_sdk/type/applicant_submit_transaction_data_request_applicant.py)<a id="applicant-applicantsubmittransactiondatarequestapplicantsumsub_python_sdktypeapplicant_submit_transaction_data_request_applicantpy"></a>


##### counterparty: [`ApplicantSubmitTransactionDataRequestCounterparty`](./sumsub_python_sdk/type/applicant_submit_transaction_data_request_counterparty.py)<a id="counterparty-applicantsubmittransactiondatarequestcounterpartysumsub_python_sdktypeapplicant_submit_transaction_data_request_counterpartypy"></a>


##### applicant_id: `str`<a id="applicant_id-str"></a>

A unique identification number of the applicant who passed user verification (KYC). If you do no have such an applicant, use [Submit transaction for non-existing applicant](ref:submit-transaction-for-non-existing-applicant) instead.

##### txn_date: `date`<a id="txn_date-date"></a>

Date and time when the transaction was initiated (format `yyyy-MM-dd HH:mm:ss+XXXX`, e.g. 2022-11-24 23:37:02+0000).

##### type: `str`<a id="type-str"></a>

A transaction type. Expects values: </br> <ul>   <li><code>finance</code>(default)</li>   <li><code>gamblingBet</code></li>   <li><code>gamblingLimitChange</code></li>   <li><code>gamblingBonusChange</code></li>   <li><code>kyc</code></li>   <li><code>travelRule</code></li>   <li><code>userPlatformEvent</code></li>   <ul>     <li><code>login</code></li>     <li><code>signup</code></li>     <li><code>passwordChange</code></li>     <li><code>twoFaReset</code></li>   </ul> </ul>

##### source_key: `str`<a id="source_key-str"></a>

A source key indication to separate access to transactions.

##### props: [`ApplicantSubmitTransactionDataRequestProps`](./sumsub_python_sdk/type/applicant_submit_transaction_data_request_props.py)<a id="props-applicantsubmittransactiondatarequestpropssumsub_python_sdktypeapplicant_submit_transaction_data_request_propspy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ApplicantSubmitTransactionDataRequest`](./sumsub_python_sdk/type/applicant_submit_transaction_data_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/applicants/{applicantId}/kyt/txns/-/data` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.applicant.submit_transaction_for_non_existing`<a id="sumsubapplicantsubmit_transaction_for_non_existing"></a>

Initiates transaction processing for non-existing applicants.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.applicant.submit_transaction_for_non_existing(
    info={
        "direction": "direction_example",
        "amount": 3.14,
        "currency_code": "currency_code_example",
    },
    txn_id="string_example",
    applicant={
        "external_user_id": "external_user_id_example",
        "full_name": "full_name_example",
        "type": "individual",
    },
    counterparty={
        "external_user_id": "external_user_id_example",
        "full_name": "full_name_example",
        "type": "individual",
    },
    level_name="levelName_example",
    txn_date="1970-01-01",
    props={},
    type="finance",
    source_key="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### info: [`ApplicantSubmitTransactionForNonExistingRequestInfo`](./sumsub_python_sdk/type/applicant_submit_transaction_for_non_existing_request_info.py)<a id="info-applicantsubmittransactionfornonexistingrequestinfosumsub_python_sdktypeapplicant_submit_transaction_for_non_existing_request_infopy"></a>


##### txn_id: `str`<a id="txn_id-str"></a>

A unique transaction identification number.

##### applicant: [`ApplicantSubmitTransactionForNonExistingRequestApplicant`](./sumsub_python_sdk/type/applicant_submit_transaction_for_non_existing_request_applicant.py)<a id="applicant-applicantsubmittransactionfornonexistingrequestapplicantsumsub_python_sdktypeapplicant_submit_transaction_for_non_existing_request_applicantpy"></a>


##### counterparty: [`ApplicantSubmitTransactionForNonExistingRequestCounterparty`](./sumsub_python_sdk/type/applicant_submit_transaction_for_non_existing_request_counterparty.py)<a id="counterparty-applicantsubmittransactionfornonexistingrequestcounterpartysumsub_python_sdktypeapplicant_submit_transaction_for_non_existing_request_counterpartypy"></a>


##### level_name: `str`<a id="level_name-str"></a>

A [verification level](https://docs.sumsub.com/reference) name. Case-sensitive and has to be created in the same environment. If contains reserved characters (e.g., `@`, `+\"`, white spaces as `%20`), it should be URL-encoded, otherwise you may get signature mismatch.

##### txn_date: `date`<a id="txn_date-date"></a>

Date and time when the transaction was initiated (format `yyyy-MM-dd HH:mm:ss+XXXX`, e.g. 2022-11-24 23:37:02+0000).

##### props: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="props-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Transaction properties. Map of strings (JSON) of custom keys and string values.

##### type: `str`<a id="type-str"></a>

A transaction type. Expects values: </br> <ul>   <li><code>finance</code>(default)</li>   <li><code>gamblingBet</code></li>   <li><code>gamblingLimitChange</code></li>   <li><code>gamblingBonusChange</code></li>   <li><code>kyc</code></li>   <li><code>travelRule</code></li>   <li><code>userPlatformEvent</code></li>   <ul>     <li><code>login</code></li>     <li><code>signup</code></li>     <li><code>passwordChange</code></li>     <li><code>twoFaReset</code></li>   </ul> </ul>

##### source_key: `str`<a id="source_key-str"></a>

A source key indication to separate access to transactions.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ApplicantSubmitTransactionForNonExistingRequest`](./sumsub_python_sdk/type/applicant_submit_transaction_for_non_existing_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/applicants/-/kyt/txns/-/data` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.applicant.update_fixed_info`<a id="sumsubapplicantupdate_fixed_info"></a>

Updates information provided when [creating an applicant](ref:create-applicants).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.applicant.update_fixed_info(
    applicant_id="applicantId_example",
    first_name="string_example",
    last_name="string_example",
    middle_name="string_example",
    first_name_en="string_example",
    last_name_en="string_example",
    middle_name_en="string_example",
    legal_name="string_example",
    gender="string_example",
    dob="string_example",
    place_of_birth="string_example",
    country_of_birth="string_example",
    state_of_birth="string_example",
    country="string_example",
    nationality="string_example",
    addresses=[
        None
    ],
    tin="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### applicant_id: `str`<a id="applicant_id-str"></a>

A unique applicant identifier.

##### first_name: `str`<a id="first_name-str"></a>

The first name of the applicant.

##### last_name: `str`<a id="last_name-str"></a>

The last name of the applicant.

##### middle_name: `str`<a id="middle_name-str"></a>

The middle name of the applicant.

##### first_name_en: `str`<a id="first_name_en-str"></a>

Automatic transliteration of the first name.

##### last_name_en: `str`<a id="last_name_en-str"></a>

Automatic transliteration of the last name.

##### middle_name_en: `str`<a id="middle_name_en-str"></a>

Automatic transliteration of the middle name.

##### legal_name: `str`<a id="legal_name-str"></a>

Legal name.

##### gender: `str`<a id="gender-str"></a>

An applicant gender (`M` or `F`).

##### dob: `str`<a id="dob-str"></a>

Applicant date of birth (format `YYYY-mm-dd`, e.g. 2001-09-25).

##### place_of_birth: `str`<a id="place_of_birth-str"></a>

The applicant birthplace.

##### country_of_birth: `str`<a id="country_of_birth-str"></a>

Applicant country of birth.

##### state_of_birth: `str`<a id="state_of_birth-str"></a>

Applicant state of birth.

##### country: `str`<a id="country-str"></a>

Alpha-3 country code (e.g. `DEU` or `GBR`).

##### nationality: `str`<a id="nationality-str"></a>

Alpha-3 country code.

##### addresses: [`ApplicantUpdateFixedInfoRequestAddresses`](./sumsub_python_sdk/type/applicant_update_fixed_info_request_addresses.py)<a id="addresses-applicantupdatefixedinforequestaddressessumsub_python_sdktypeapplicant_update_fixed_info_request_addressespy"></a>

##### tin: `str`<a id="tin-str"></a>

Tax identification number.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ApplicantUpdateFixedInfoRequest`](./sumsub_python_sdk/type/applicant_update_fixed_info_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/applicants/{applicantId}/fixedInfo` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.applicant.update_top_level_info`<a id="sumsubapplicantupdate_top_level_info"></a>

Changes existing verification level configuration.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.applicant.update_top_level_info(
    id="string_example",
    external_user_id="string_example",
    email="string_example",
    phone="string_example",
    source_key="string_example",
    lang="string_example",
    questionnaires=[
        None
    ],
    metadata=[
        None
    ],
    deleted=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

A unique applicant identifier.

##### external_user_id: `str`<a id="external_user_id-str"></a>

An external applicant identifier.

##### email: `str`<a id="email-str"></a>

A new email address that you want to assign to the given applicant.

##### phone: `str`<a id="phone-str"></a>

A new phone number that you want to assign to the given applicant.

##### source_key: `str`<a id="source_key-str"></a>

A new [source key](https://docs.sumsub.com/reference) that you want to assign to the given applicant.

##### lang: `str`<a id="lang-str"></a>

The language, in which the applicant should see the verification results.

##### questionnaires: [`ApplicantUpdateTopLevelInfoRequestQuestionnaires`](./sumsub_python_sdk/type/applicant_update_top_level_info_request_questionnaires.py)<a id="questionnaires-applicantupdatetoplevelinforequestquestionnairessumsub_python_sdktypeapplicant_update_top_level_info_request_questionnairespy"></a>

##### metadata: [`ApplicantUpdateTopLevelInfoRequestMetadata`](./sumsub_python_sdk/type/applicant_update_top_level_info_request_metadata.py)<a id="metadata-applicantupdatetoplevelinforequestmetadatasumsub_python_sdktypeapplicant_update_top_level_info_request_metadatapy"></a>

##### deleted: `bool`<a id="deleted-bool"></a>

Marks an applicant as inactive if set to `true`. The applicant will not be considered a duplicate. SDKs will not initiate checks for this applicant.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ApplicantUpdateTopLevelInfoRequest`](./sumsub_python_sdk/type/applicant_update_top_level_info_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/applicants` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.audit_trail_event.get_events`<a id="sumsubaudit_trail_eventget_events"></a>

Returns audit trail events.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.audit_trail_event.get_events(
    subject_name="string_example",
    activity="string_example",
    _from="string_example",
    to="string_example",
    limit="10",
    offset="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### subject_name: `str`<a id="subject_name-str"></a>

The name of the subject for which events are received. If the name is not specified, events are received for all subjects on the key.

##### activity: `str`<a id="activity-str"></a>

If specified, only events with this activity will be in the response.

##### _from: `str`<a id="_from-str"></a>

From the date/time events are received (format yyyy-MM-dd HH:mm:ss, e.g. 2022-10-01 12:05:00). If it's not specified - events are received from yesterday.

##### to: `str`<a id="to-str"></a>

To the date/time events are received (format yyyy-MM-dd HH:mm:ss, e.g. 2022-10-01 12:15:00). If it's not specified - events are received up to now.

##### limit: `str`<a id="limit-str"></a>

Max number of events in one request. Can't be more than 20000. By default is 10.

##### offset: `str`<a id="offset-str"></a>

Allows to skip the offset events before beginning to return the events. By default is 0.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/auditTrailEvents` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.check.additional_company_data`<a id="sumsubcheckadditional_company_data"></a>

Returns company check results.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.check.additional_company_data(
    applicant_id="applicantId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### applicant_id: `str`<a id="applicant_id-str"></a>

A unique applicant identifier.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/checks/latest?type&#x3D;COMPANY` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.check.additional_poa_data`<a id="sumsubcheckadditional_poa_data"></a>

Returns PoA data.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.check.additional_poa_data(
    applicant_id="applicantId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### applicant_id: `str`<a id="applicant_id-str"></a>

A unique applicant identifier.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/checks/latest?type&#x3D;POA` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.check.email_confirmation_results`<a id="sumsubcheckemail_confirmation_results"></a>

Returns email confirmation check results.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.check.email_confirmation_results(
    applicant_id="applicantId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### applicant_id: `str`<a id="applicant_id-str"></a>

A unique applicant identifier.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/checks/latest?type&#x3D;EMAIL_CONFIRMATION` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.check.ip_check_results`<a id="sumsubcheckip_check_results"></a>

Returns IP check results.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.check.ip_check_results(
    applicant_id="applicantId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### applicant_id: `str`<a id="applicant_id-str"></a>

A unique applicant identifier.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/checks/latest?type&#x3D;IP_CHECK` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.check.perform_name_cross_validation`<a id="sumsubcheckperform_name_cross_validation"></a>

Performs a name cross validation.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.check.perform_name_cross_validation(
    id_docs=[
        {
            "first_name": "first_name_example",
        }
    ],
    comparison_mode="comparisonMode_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_docs: [`CheckPerformNameCrossValidationRequestIdDocs`](./sumsub_python_sdk/type/check_perform_name_cross_validation_request_id_docs.py)<a id="id_docs-checkperformnamecrossvalidationrequestiddocssumsub_python_sdktypecheck_perform_name_cross_validation_request_id_docspy"></a>

##### comparison_mode: `str`<a id="comparison_mode-str"></a>

Data comparison mode. See the [possible values](/reference/perform-name-cross-validation#possible-comparisonmode-values).

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CheckPerformNameCrossValidationRequest`](./sumsub_python_sdk/type/check_perform_name_cross_validation_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/checks/crossCheck?comparisonMode&#x3D;{comparisonMode}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.check.phone_confirmation_results`<a id="sumsubcheckphone_confirmation_results"></a>

Returns phone confirmation check results.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.check.phone_confirmation_results(
    applicant_id="applicantId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### applicant_id: `str`<a id="applicant_id-str"></a>

A unique applicant identifier.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/checks/latest?type&#x3D;PHONE_CONFIRMATION` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.check.tin_ssn_check_results`<a id="sumsubchecktin_ssn_check_results"></a>

Returns TIN (SSN) check results.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.check.tin_ssn_check_results(
    applicant_id="applicantId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### applicant_id: `str`<a id="applicant_id-str"></a>

A unique applicant identification number.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/checks/latest?type&#x3D;TIN` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.health.status_api_get`<a id="sumsubhealthstatus_api_get"></a>

API health

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.health.status_api_get()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/status/api` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.image.get_document_images`<a id="sumsubimageget_document_images"></a>

Returns document images.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.image.get_document_images(
    inspection_id="inspectionId_example",
    image_id="imageId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### inspection_id: `str`<a id="inspection_id-str"></a>

An inspection identifier. This identifier is returned as a root field upon running [this API method](ref:get-applicant-data).

##### image_id: `str`<a id="image_id-str"></a>

An image identifier. You can get this number by using [this API method](ref:get-applicant-verification-steps-status).

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/inspections/{inspectionId}/resources/{imageId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.image.mark_as_inactive`<a id="sumsubimagemark_as_inactive"></a>

Marks uploaded images as deleted.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.image.mark_as_inactive(
    inspection_id="inspectionId_example",
    image_id="imageId_example",
    revert=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### inspection_id: `str`<a id="inspection_id-str"></a>

An inspection identifier. You can get this number by using [this API method](ref:get-applicant-data).

##### image_id: `str`<a id="image_id-str"></a>

An image identifier. You can get this number by using [this API method](ref:get-applicant-verification-steps-status).

##### revert: `bool`<a id="revert-bool"></a>

Set `true` to revert inactivity of the image.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/inspections/{inspectionId}/resources/{imageId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.inspection.get_video_ident_data`<a id="sumsubinspectionget_video_ident_data"></a>

Returns the video call results.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.inspection.get_video_ident_data(
    inspection_id="inspectionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### inspection_id: `str`<a id="inspection_id-str"></a>

A unique inspection identifier.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/inspections/{inspectionId}?fields&#x3D;videoIdentData` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.note.add_to_transaction`<a id="sumsubnoteadd_to_transaction"></a>

Adds notes to transactions.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.note.add_to_transaction(
    txn_id="string_example",
    note="string_example",
    tags=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### txn_id: `str`<a id="txn_id-str"></a>

A unique transaction identifier.

##### note: `str`<a id="note-str"></a>

A note to add.

##### tags: [`NoteAddToTransactionRequestTags`](./sumsub_python_sdk/type/note_add_to_transaction_request_tags.py)<a id="tags-noteaddtotransactionrequesttagssumsub_python_sdktypenote_add_to_transaction_request_tagspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`NoteAddToTransactionRequest`](./sumsub_python_sdk/type/note_add_to_transaction_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/kyt/txns/notes` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.note.get_transaction_notes`<a id="sumsubnoteget_transaction_notes"></a>

Returns transaction notes.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.note.get_transaction_notes(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

A unique transaction identifier.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/kyt/txns/{id}/notes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.note.remove_from_transaction`<a id="sumsubnoteremove_from_transaction"></a>

Removes notes from transactions.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.note.remove_from_transaction(
    txn_id="string_example",
    id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### txn_id: `str`<a id="txn_id-str"></a>

A unique transaction identifier.

##### id: `str`<a id="id-str"></a>

A unique note identifier.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`NoteRemoveFromTransactionRequest`](./sumsub_python_sdk/type/note_remove_from_transaction_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/kyt/txns/notes` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.note.update_transaction_notes`<a id="sumsubnoteupdate_transaction_notes"></a>

Updates a note.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.note.update_transaction_notes(
    txn_id="string_example",
    id="string_example",
    note="string_example",
    tags=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### txn_id: `str`<a id="txn_id-str"></a>

A unique transaction identifier.

##### id: `str`<a id="id-str"></a>

A unique note identifier.

##### note: `str`<a id="note-str"></a>

A new note.

##### tags: [`NoteUpdateTransactionNotesRequestTags`](./sumsub_python_sdk/type/note_update_transaction_notes_request_tags.py)<a id="tags-noteupdatetransactionnotesrequesttagssumsub_python_sdktypenote_update_transaction_notes_request_tagspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`NoteUpdateTransactionNotesRequest`](./sumsub_python_sdk/type/note_update_transaction_notes_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/kyt/txns/notes` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.tag.add_transaction_tags`<a id="sumsubtagadd_transaction_tags"></a>

Adds tags to transactions.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.tag.add_transaction_tags(
    id="id_example",
    raw_body=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

A unique transaction identifier.

##### raw_body: [`TagAddTransactionTagsRequestRawBody`](./sumsub_python_sdk/type/tag_add_transaction_tags_request_raw_body.py)<a id="raw_body-tagaddtransactiontagsrequestrawbodysumsub_python_sdktypetag_add_transaction_tags_request_raw_bodypy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TagAddTransactionTagsRequest`](./sumsub_python_sdk/type/tag_add_transaction_tags_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/kyt/txns/{id}/tags` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.token.create_action_token`<a id="sumsubtokencreate_action_token"></a>

Creates an applicant action token.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.token.create_action_token(
    user_id="userId_example",
    external_action_id="externalActionId_example",
    level_name="levelName_example",
    ttl_in_secs="600",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

An external user ID which will be bound to the token.

##### external_action_id: `str`<a id="external_action_id-str"></a>

An external action ID which will be bound to the token.

##### level_name: `str`<a id="level_name-str"></a>

The name of the [verification level](https://docs.sumsub.com/reference).

##### ttl_in_secs: `str`<a id="ttl_in_secs-str"></a>

A lifespan of a token in seconds. Default value is 10 mins.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/accessTokens` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.token.get_available_currencies`<a id="sumsubtokenget_available_currencies"></a>

Returns available tokens.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.token.get_available_currencies()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/standalone/crypto/availableCurrencies` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.transaction.approve_reject`<a id="sumsubtransactionapprove_reject"></a>

Approves or rejects transactions.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.transaction.approve_reject(
    id="id_example",
    review_answer="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

A unique transaction identification number.

##### review_answer: `str`<a id="review_answer-str"></a>

Sets the review answer. Can be `GREEN` or `RED`.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TransactionApproveRejectRequest`](./sumsub_python_sdk/type/transaction_approve_reject_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/kyt/txns/{id}/review/status/completed` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.transaction.bulk_import`<a id="sumsubtransactionbulk_import"></a>

Imports a list of transactions.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.transaction.bulk_import(
    applicant_id="string_example",
    data={
        "txn_id": "txn_id_example",
    },
    ignore_errors=False,
    score_saved_txns=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### applicant_id: `str`<a id="applicant_id-str"></a>

A unique identification number of the applicant who passed user verification (KYC).

##### data: [`TransactionBulkImportRequestData`](./sumsub_python_sdk/type/transaction_bulk_import_request_data.py)<a id="data-transactionbulkimportrequestdatasumsub_python_sdktypetransaction_bulk_import_request_datapy"></a>


##### ignore_errors: `bool`<a id="ignore_errors-bool"></a>

<ul><li><code>true</code> — all valid transactions will be created and returned, errors will be ignored during the processing and listed in the response.</li><li><code>false</code> (default) — valid transactions will be created up to the first detected error. The response will only contain the error on which the processing was interrupted.</li></ul>

##### score_saved_txns: `bool`<a id="score_saved_txns-bool"></a>

Allows you to control whether scoring should be run on imported transactions or not:<ul><li><code>true</code> (default) — start scoring after import.</li><li><code>false</code> — do not start scoring after import.</li></ul>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TransactionBulkImportRequest`](./sumsub_python_sdk/type/transaction_bulk_import_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/kyt/misc/txns/import` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.transaction.confirm_ownership`<a id="sumsubtransactionconfirm_ownership"></a>

Confirms that the specified transaction belongs to your exchange (VASP).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.transaction.confirm_ownership(
    txn_id="txnId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### txn_id: `str`<a id="txn_id-str"></a>

A unique transaction identifier.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/kyt/txns/{txnId}/ownership/confirmed` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.transaction.get_one_data`<a id="sumsubtransactionget_one_data"></a>

Returns transaction information based on the provided `externalTxnId`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.transaction.get_one_data(
    external_txn_id="externalTxnId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### external_txn_id: `str`<a id="external_txn_id-str"></a>

A unique transaction identifier on your side.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/kyt/txns/-;data.txnId&#x3D;{externalTxnId}/one` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.transaction.information_one`<a id="sumsubtransactioninformation_one"></a>

Returns transaction information.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.transaction.information_one(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

A unique transaction identifier.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/kyt/txns/{id}/one` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.transaction.list_tags`<a id="sumsubtransactionlist_tags"></a>

Returns a list of transaction tags.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.transaction.list_tags(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

A unique transaction identifier.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/kyt/txns/{id}/tags` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.transaction.re_score`<a id="sumsubtransactionre_score"></a>

Re-scores transactions.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.transaction.re_score(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

A unique transaction identification number.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/kyt/txns/{id}/-/score` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.transaction.remove_ownership`<a id="sumsubtransactionremove_ownership"></a>

Removes the ownership from a previously confirmed transaction.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.transaction.remove_ownership(
    txn_id="txnId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### txn_id: `str`<a id="txn_id-str"></a>

A unique transaction identifier.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/kyt/txns/{txnId}/ownership/unconfirmed` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.transaction.remove_tags`<a id="sumsubtransactionremove_tags"></a>

Removes tags from transactions.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.transaction.remove_tags(
    id="id_example",
    raw_body=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

A unique transaction identifier.

##### raw_body: [`TransactionRemoveTagsRequestRawBody`](./sumsub_python_sdk/type/transaction_remove_tags_request_raw_body.py)<a id="raw_body-transactionremovetagsrequestrawbodysumsub_python_sdktypetransaction_remove_tags_request_raw_bodypy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TransactionRemoveTagsRequest`](./sumsub_python_sdk/type/transaction_remove_tags_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/kyt/txns/{id}/tags` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.transaction.update_blockchain_info`<a id="sumsubtransactionupdate_blockchain_info"></a>

Updates information from the blockchain.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_blockchain_info_response = sumsub.transaction.update_blockchain_info(
    txn_id="txnId_example",
    fingerprint="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### txn_id: `str`<a id="txn_id-str"></a>

A unique transaction identifier.

##### fingerprint: `str`<a id="fingerprint-str"></a>

A crypto transaction ID received from the blockchain.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TransactionUpdateBlockchainInfoRequest`](./sumsub_python_sdk/type/transaction_update_blockchain_info_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/kyt/txns/{txnId}/data/info` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.transaction.update_properties`<a id="sumsubtransactionupdate_properties"></a>

Updates transaction properties.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.transaction.update_properties(
    custom_property="newValue",
    id="id_example",
    unset_keys="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### custom_property: `str`<a id="custom_property-str"></a>

##### id: `str`<a id="id-str"></a>

A unique transaction identification number.

##### unset_keys: `str`<a id="unset_keys-str"></a>

A list of property names separated by commas that should be set to `null`.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TransactionUpdatePropertiesRequest`](./sumsub_python_sdk/type/transaction_update_properties_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/kyt/txns/{id}/props` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.vasp.get_available_vasps`<a id="sumsubvaspget_available_vasps"></a>

Returns a list of VASPs from the Sumsub VASP directory.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_available_vasps_response = sumsub.vasp.get_available_vasps(
    limit=10,
    offset=0,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

Maximum number of the VASPs to be returned. The maximum recommended value you can set is 100.

##### offset: `int`<a id="offset-int"></a>

Offset of the VASPs to be returned.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/vasps/-` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `sumsub.web_sdk_link.generate_external`<a id="sumsubweb_sdk_linkgenerate_external"></a>

Creates a link to WebSDK for the specified applicant.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
sumsub.web_sdk_link.generate_external(
    level_name="levelName_example",
    ttl_in_secs=1,
    external_user_id="string_example",
    lang="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### level_name: `str`<a id="level_name-str"></a>

A [verification level](https://docs.sumsub.com/reference) name. Case-sensitive and has to be created in the same environment. If contains reserved characters (e.g., `@`, `+\"`, white spaces as `%20`), it should be URL-encoded, otherwise you may get signature mismatch.

##### ttl_in_secs: `int`<a id="ttl_in_secs-int"></a>

A lifespan of the link in seconds.

##### external_user_id: `str`<a id="external_user_id-str"></a>

An external user ID on your side.

##### lang: `str`<a id="lang-str"></a>

The language for WebSDK in ISO 639-1 format.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/resources/sdkIntegrations/levels/{levelName}/websdkLink` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
