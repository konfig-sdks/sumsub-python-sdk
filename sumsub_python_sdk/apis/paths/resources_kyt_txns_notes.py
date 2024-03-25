from sumsub_python_sdk.paths.resources_kyt_txns_notes.post import ApiForpost
from sumsub_python_sdk.paths.resources_kyt_txns_notes.delete import ApiFordelete
from sumsub_python_sdk.paths.resources_kyt_txns_notes.patch import ApiForpatch


class ResourcesKytTxnsNotes(
    ApiForpost,
    ApiFordelete,
    ApiForpatch,
):
    pass
