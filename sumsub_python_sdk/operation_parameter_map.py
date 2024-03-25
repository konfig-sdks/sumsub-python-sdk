operation_parameter_map = {
    '/resources/standalone/crypto/cryptoSourceOfFunds-POST': {
        'parameters': [
            {
                'name': 'currency'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'address'
            },
            {
                'name': 'txn'
            },
            {
                'name': 'tokenId'
            },
        ]
    },
    '/resources/applicants/{applicantId}/info/companyInfo/beneficiaries-POST': {
        'parameters': [
            {
                'name': 'applicant'
            },
            {
                'name': 'applicantId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'applicantId'
            },
            {
                'name': 'positions'
            },
        ]
    },
    '/resources/applicants/{applicantId}/agreement-POST': {
        'parameters': [
            {
                'name': 'records'
            },
            {
                'name': 'applicantId'
            },
            {
                'name': 'acceptedAt'
            },
            {
                'name': 'residenceCountry'
            },
        ]
    },
    '/resources/applicants/{applicantId}/tags/add-POST': {
        'parameters': [
            {
                'name': 'applicantId'
            },
            {
                'name': 'RAW_BODY'
            },
        ]
    },
    '/resources/applicants/{applicantId}/tags-POST': {
        'parameters': [
            {
                'name': 'applicantId'
            },
            {
                'name': 'RAW_BODY'
            },
        ]
    },
    '/resources/applicants/{applicantId}/info/idDoc-POST': {
        'parameters': [
            {
                'name': 'X-Return-Doc-Warnings'
            },
            {
                'name': 'applicantId'
            },
            {
                'name': 'metadata'
            },
            {
                'name': 'content'
            },
        ]
    },
    '/resources/applicantActions/{actionId}/images-POST': {
        'parameters': [
            {
                'name': 'content'
            },
            {
                'name': 'metadata'
            },
            {
                'name': 'actionId'
            },
        ]
    },
    '/resources/applicantActions/{actionId}/paymentMethod-POST': {
        'parameters': [
            {
                'name': 'type'
            },
            {
                'name': 'actionId'
            },
            {
                'name': 'subType'
            },
            {
                'name': 'data'
            },
        ]
    },
    '/resources/applicants/{applicantId}/blacklist?note={note}-POST': {
        'parameters': [
            {
                'name': 'note'
            },
            {
                'name': 'applicantId'
            },
        ]
    },
    '/resources/applicants/{applicantId}/info/companyInfo-PATCH': {
        'parameters': [
            {
                'name': 'companyName'
            },
            {
                'name': 'registrationNumber'
            },
            {
                'name': 'applicantId'
            },
            {
                'name': 'country'
            },
            {
                'name': 'legalAddress'
            },
            {
                'name': 'incorporatedOn'
            },
            {
                'name': 'type'
            },
            {
                'name': 'email'
            },
            {
                'name': 'controlScheme'
            },
            {
                'name': 'phone'
            },
            {
                'name': 'taxId'
            },
            {
                'name': 'registrationLocation'
            },
            {
                'name': 'website'
            },
            {
                'name': 'postalAddress'
            },
            {
                'name': 'beneficiaries'
            },
            {
                'name': 'addresses'
            },
        ]
    },
    '/resources/applicants/{applicantId}/info-PATCH': {
        'parameters': [
            {
                'name': 'applicantId'
            },
            {
                'name': 'firstName'
            },
            {
                'name': 'lastName'
            },
            {
                'name': 'middleName'
            },
            {
                'name': 'legalName'
            },
            {
                'name': 'gender'
            },
            {
                'name': 'dob'
            },
            {
                'name': 'placeOfBirth'
            },
            {
                'name': 'countryOfBirth'
            },
            {
                'name': 'stateOfBirth'
            },
            {
                'name': 'country'
            },
            {
                'name': 'nationality'
            },
            {
                'name': 'addresses'
            },
            {
                'name': 'tin'
            },
        ]
    },
    '/resources/applicants/{applicantId}/moveToLevel-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'applicantId'
            },
        ]
    },
    '/resources/moderationStates/-;applicantId={applicantId}-GET': {
        'parameters': [
            {
                'name': 'applicantId'
            },
        ]
    },
    '/resources/applicants/{applicantId}/ekyc/confirm/{confirmationid}-POST': {
        'parameters': [
            {
                'name': 'applicantId'
            },
            {
                'name': 'confirmationId'
            },
            {
                'name': 'otp'
            },
            {
                'name': 'oauth'
            },
        ]
    },
    '/resources/applicantActions/-/forApplicant/{applicantId}?levelName={levelName}-POST': {
        'parameters': [
            {
                'name': 'externalActionId'
            },
            {
                'name': 'applicantId'
            },
            {
                'name': 'levelName'
            },
            {
                'name': 'paymentMethod'
            },
            {
                'name': 'email'
            },
            {
                'name': 'phone'
            },
        ]
    },
    '/resources/applicantActions/-/forApplicant/{applicantId}/cryptoSourceOfFunds-POST': {
        'parameters': [
            {
                'name': 'currency'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'address'
            },
            {
                'name': 'applicantId'
            },
            {
                'name': 'txn'
            },
            {
                'name': 'tokenId'
            },
        ]
    },
    '/resources/applicantActions/-/forApplicant/{applicantId}/?levelName=paymentSource-POST': {
        'parameters': [
            {
                'name': 'applicantId'
            },
            {
                'name': 'levelName'
            },
            {
                'name': 'externalActionId'
            },
            {
                'name': 'paymentSource'
            },
        ]
    },
    '/resources/applicants/{applicantId}/presence/{status}-PATCH': {
        'parameters': [
            {
                'name': 'applicantId'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/resources/kyt/txns/{txnId}/data/applicant-PATCH': {
        'parameters': [
            {
                'name': 'fullName'
            },
            {
                'name': 'txnId'
            },
        ]
    },
    '/resources/applicantActions/{actionId}/one-GET': {
        'parameters': [
            {
                'name': 'actionId'
            },
        ]
    },
    '/resources/applicantActions/-;applicantId={applicantId}-GET': {
        'parameters': [
            {
                'name': 'applicantId'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
        ]
    },
    '/resources/applicantActions/{actionId}/images/{imageId}?preview={isPreview}-GET': {
        'parameters': [
            {
                'name': 'actionId'
            },
            {
                'name': 'imageId'
            },
            {
                'name': 'isPreview'
            },
        ]
    },
    '/resources/applicants/{applicantId}/one-GET': {
        'parameters': [
            {
                'name': 'applicantId'
            },
        ]
    },
    '/resources/applicants/-;externalUserId={externalUserId}/one-GET': {
        'parameters': [
            {
                'name': 'externalUserId'
            },
        ]
    },
    '/resources/checks/latest-GET': {
        'parameters': [
            {
                'name': 'type'
            },
            {
                'name': 'applicantId'
            },
        ]
    },
    '/resources/applicantFraudNetworks/{networkId}/one-GET': {
        'parameters': [
            {
                'name': 'networkId'
            },
        ]
    },
    '/resources/applicantFraudNetworks-GET': {
        'parameters': [
            {
                'name': 'offset'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/resources/applicantFraudNetworks/-/byApplicant/{applicantId}-GET': {
        'parameters': [
            {
                'name': 'applicantId'
            },
        ]
    },
    '/resources/applicants/-/levels-GET': {
        'parameters': [
        ]
    },
    '/resources/applicants/{applicantId}/requiredIdDocs-POST': {
        'parameters': [
            {
                'name': 'applicantId'
            },
        ]
    },
    '/resources/applicants/{applicantId}/status-GET': {
        'parameters': [
            {
                'name': 'applicantId'
            },
        ]
    },
    '/resources/applicants/{applicantId}/requiredIdDocsStatus-GET': {
        'parameters': [
            {
                'name': 'applicantId'
            },
        ]
    },
    '/resources/videoIdent/applicant/{applicantId}/media/{compositionMediaId}-GET': {
        'parameters': [
            {
                'name': 'applicantId'
            },
            {
                'name': 'compositionMediaId'
            },
        ]
    },
    '/resources/applicants/-/applicantImport-POST': {
        'parameters': [
            {
                'name': 'content'
            },
        ]
    },
    '/resources/applicants/-/ingestCompleted?levelName={levelName}-POST': {
        'parameters': [
            {
                'name': 'info'
            },
            {
                'name': 'externalUserId'
            },
            {
                'name': 'review'
            },
            {
                'name': 'levelName'
            },
        ]
    },
    '/resources/applicants/{applicantId}/status/pending?reason={reason}-POST': {
        'parameters': [
            {
                'name': 'applicantId'
            },
            {
                'name': 'reason'
            },
        ]
    },
    '/resources/kyt/txns/{txnId}/applicantId/{applicantId}-POST': {
        'parameters': [
            {
                'name': 'txnId'
            },
            {
                'name': 'applicantId'
            },
        ]
    },
    '/resources/applicants/{applicantId}/tags-DELETE': {
        'parameters': [
            {
                'name': 'applicantId'
            },
            {
                'name': 'RAW_BODY'
            },
        ]
    },
    '/resources/applicants/{applicantId}/info/companyInfo/beneficiaries/{beneficiaryApplicantId}-DELETE': {
        'parameters': [
            {
                'name': 'applicantId'
            },
            {
                'name': 'beneficiaryApplicantId'
            },
        ]
    },
    '/resources/applicantActions/{actionId}/review/status/pending-POST': {
        'parameters': [
            {
                'name': 'actionId'
            },
        ]
    },
    '/resources/applicants/{applicantId}/reset-POST': {
        'parameters': [
            {
                'name': 'applicantId'
            },
        ]
    },
    '/resources/applicants/{applicantId}/resetStep/{idDocSetType}-POST': {
        'parameters': [
            {
                'name': 'applicantId'
            },
            {
                'name': 'idDocSetType'
            },
        ]
    },
    '/resources/applicants/{applicantId}/status/testCompleted-POST': {
        'parameters': [
            {
                'name': 'reviewAnswer'
            },
            {
                'name': 'rejectLabels'
            },
            {
                'name': 'applicantId'
            },
            {
                'name': 'reviewRejectType'
            },
            {
                'name': 'clientComment'
            },
            {
                'name': 'moderationComment'
            },
        ]
    },
    '/resources/applicants/{applicantId}/ekyc/submit-POST': {
        'parameters': [
            {
                'name': 'info'
            },
            {
                'name': 'applicantId'
            },
        ]
    },
    '/resources/applicantActions/-/forApplicant/{applicantId}/paymentMethod-POST': {
        'parameters': [
            {
                'name': 'X-External-Action-Id'
            },
            {
                'name': 'applicantId'
            },
            {
                'name': 'requireSelfie'
            },
        ]
    },
    '/resources/applicants/{applicantId}/kyt/txns/-/data-POST': {
        'parameters': [
            {
                'name': 'info'
            },
            {
                'name': 'txnId'
            },
            {
                'name': 'applicant'
            },
            {
                'name': 'counterparty'
            },
            {
                'name': 'applicantId'
            },
            {
                'name': 'txnDate'
            },
            {
                'name': 'type'
            },
            {
                'name': 'sourceKey'
            },
            {
                'name': 'props'
            },
        ]
    },
    '/resources/applicants/-/kyt/txns/-/data-POST': {
        'parameters': [
            {
                'name': 'info'
            },
            {
                'name': 'txnId'
            },
            {
                'name': 'applicant'
            },
            {
                'name': 'counterparty'
            },
            {
                'name': 'levelName'
            },
            {
                'name': 'txnDate'
            },
            {
                'name': 'props'
            },
            {
                'name': 'type'
            },
            {
                'name': 'sourceKey'
            },
        ]
    },
    '/resources/applicants/{applicantId}/fixedInfo-PATCH': {
        'parameters': [
            {
                'name': 'applicantId'
            },
            {
                'name': 'firstName'
            },
            {
                'name': 'lastName'
            },
            {
                'name': 'middleName'
            },
            {
                'name': 'firstNameEn'
            },
            {
                'name': 'lastNameEn'
            },
            {
                'name': 'middleNameEn'
            },
            {
                'name': 'legalName'
            },
            {
                'name': 'gender'
            },
            {
                'name': 'dob'
            },
            {
                'name': 'placeOfBirth'
            },
            {
                'name': 'countryOfBirth'
            },
            {
                'name': 'stateOfBirth'
            },
            {
                'name': 'country'
            },
            {
                'name': 'nationality'
            },
            {
                'name': 'addresses'
            },
            {
                'name': 'tin'
            },
        ]
    },
    '/resources/applicants-PATCH': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'externalUserId'
            },
            {
                'name': 'email'
            },
            {
                'name': 'phone'
            },
            {
                'name': 'sourceKey'
            },
            {
                'name': 'lang'
            },
            {
                'name': 'questionnaires'
            },
            {
                'name': 'metadata'
            },
            {
                'name': 'deleted'
            },
        ]
    },
    '/resources/auditTrailEvents-GET': {
        'parameters': [
            {
                'name': 'subjectName'
            },
            {
                'name': 'activity'
            },
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
        ]
    },
    '/resources/checks/latest?type=COMPANY-GET': {
        'parameters': [
            {
                'name': 'applicantId'
            },
        ]
    },
    '/resources/checks/latest?type=POA-GET': {
        'parameters': [
            {
                'name': 'applicantId'
            },
        ]
    },
    '/resources/checks/latest?type=EMAIL_CONFIRMATION-GET': {
        'parameters': [
            {
                'name': 'applicantId'
            },
        ]
    },
    '/resources/checks/latest?type=IP_CHECK-GET': {
        'parameters': [
            {
                'name': 'applicantId'
            },
        ]
    },
    '/resources/checks/crossCheck?comparisonMode={comparisonMode}-POST': {
        'parameters': [
            {
                'name': 'idDocs'
            },
            {
                'name': 'comparisonMode'
            },
        ]
    },
    '/resources/checks/latest?type=PHONE_CONFIRMATION-GET': {
        'parameters': [
            {
                'name': 'applicantId'
            },
        ]
    },
    '/resources/checks/latest?type=TIN-GET': {
        'parameters': [
            {
                'name': 'applicantId'
            },
        ]
    },
    '/resources/status/api-GET': {
        'parameters': [
        ]
    },
    '/resources/inspections/{inspectionId}/resources/{imageId}-GET': {
        'parameters': [
            {
                'name': 'inspectionId'
            },
            {
                'name': 'imageId'
            },
        ]
    },
    '/resources/inspections/{inspectionId}/resources/{imageId}-DELETE': {
        'parameters': [
            {
                'name': 'inspectionId'
            },
            {
                'name': 'imageId'
            },
            {
                'name': 'revert'
            },
        ]
    },
    '/resources/inspections/{inspectionId}?fields=videoIdentData-GET': {
        'parameters': [
            {
                'name': 'inspectionId'
            },
        ]
    },
    '/resources/kyt/txns/notes-POST': {
        'parameters': [
            {
                'name': 'txnId'
            },
            {
                'name': 'note'
            },
            {
                'name': 'tags'
            },
        ]
    },
    '/resources/kyt/txns/{id}/notes-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/resources/kyt/txns/notes-DELETE': {
        'parameters': [
            {
                'name': 'txnId'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/resources/kyt/txns/notes-PATCH': {
        'parameters': [
            {
                'name': 'txnId'
            },
            {
                'name': 'id'
            },
            {
                'name': 'note'
            },
            {
                'name': 'tags'
            },
        ]
    },
    '/resources/kyt/txns/{id}/tags-POST': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'RAW_BODY'
            },
        ]
    },
    '/resources/accessTokens-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'externalActionId'
            },
            {
                'name': 'levelName'
            },
            {
                'name': 'ttlInSecs'
            },
        ]
    },
    '/resources/standalone/crypto/availableCurrencies-GET': {
        'parameters': [
        ]
    },
    '/resources/kyt/txns/{id}/review/status/completed-POST': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'reviewAnswer'
            },
        ]
    },
    '/resources/kyt/misc/txns/import-POST': {
        'parameters': [
            {
                'name': 'applicantId'
            },
            {
                'name': 'data'
            },
            {
                'name': 'ignoreErrors'
            },
            {
                'name': 'scoreSavedTxns'
            },
        ]
    },
    '/resources/kyt/txns/{txnId}/ownership/confirmed-POST': {
        'parameters': [
            {
                'name': 'txnId'
            },
        ]
    },
    '/resources/kyt/txns/-;data.txnId={externalTxnId}/one-GET': {
        'parameters': [
            {
                'name': 'externalTxnId'
            },
        ]
    },
    '/resources/kyt/txns/{id}/one-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/resources/kyt/txns/{id}/tags-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/resources/kyt/txns/{id}/-/score-POST': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/resources/kyt/txns/{txnId}/ownership/unconfirmed-POST': {
        'parameters': [
            {
                'name': 'txnId'
            },
        ]
    },
    '/resources/kyt/txns/{id}/tags-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'RAW_BODY'
            },
        ]
    },
    '/resources/kyt/txns/{txnId}/data/info-PATCH': {
        'parameters': [
            {
                'name': 'txnId'
            },
            {
                'name': 'fingerprint'
            },
        ]
    },
    '/resources/kyt/txns/{id}/props-PATCH': {
        'parameters': [
            {
                'name': 'customProperty'
            },
            {
                'name': 'id'
            },
            {
                'name': 'unsetKeys'
            },
        ]
    },
    '/resources/vasps/--GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
        ]
    },
    '/resources/sdkIntegrations/levels/{levelName}/websdkLink-POST': {
        'parameters': [
            {
                'name': 'levelName'
            },
            {
                'name': 'ttlInSecs'
            },
            {
                'name': 'externalUserId'
            },
            {
                'name': 'lang'
            },
        ]
    },
};