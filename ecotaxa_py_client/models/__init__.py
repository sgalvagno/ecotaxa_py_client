# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from ecotaxa_py_client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from ecotaxa_py_client.model.acquisition_model import AcquisitionModel
from ecotaxa_py_client.model.body_export_object_set_object_set_export_post import BodyExportObjectSetObjectSetExportPost
from ecotaxa_py_client.model.bulk_update_req import BulkUpdateReq
from ecotaxa_py_client.model.classify_auto_req import ClassifyAutoReq
from ecotaxa_py_client.model.classify_req import ClassifyReq
from ecotaxa_py_client.model.collection_model import CollectionModel
from ecotaxa_py_client.model.constants import Constants
from ecotaxa_py_client.model.create_collection_req import CreateCollectionReq
from ecotaxa_py_client.model.create_project_req import CreateProjectReq
from ecotaxa_py_client.model.directory_entry_model import DirectoryEntryModel
from ecotaxa_py_client.model.directory_model import DirectoryModel
from ecotaxa_py_client.model.emo_dnet_export_rsp import EMODnetExportRsp
from ecotaxa_py_client.model.export_req import ExportReq
from ecotaxa_py_client.model.export_rsp import ExportRsp
from ecotaxa_py_client.model.export_type_enum import ExportTypeEnum
from ecotaxa_py_client.model.group_definitions import GroupDefinitions
from ecotaxa_py_client.model.http_validation_error import HTTPValidationError
from ecotaxa_py_client.model.historical_classification import HistoricalClassification
from ecotaxa_py_client.model.historical_last_classif import HistoricalLastClassif
from ecotaxa_py_client.model.image_model import ImageModel
from ecotaxa_py_client.model.import_req import ImportReq
from ecotaxa_py_client.model.import_rsp import ImportRsp
from ecotaxa_py_client.model.job_model import JobModel
from ecotaxa_py_client.model.limit_methods import LimitMethods
from ecotaxa_py_client.model.login_req import LoginReq
from ecotaxa_py_client.model.merge_rsp import MergeRsp
from ecotaxa_py_client.model.minimal_user_bo import MinimalUserBO
from ecotaxa_py_client.model.object_header_model import ObjectHeaderModel
from ecotaxa_py_client.model.object_model import ObjectModel
from ecotaxa_py_client.model.object_set_query_rsp import ObjectSetQueryRsp
from ecotaxa_py_client.model.object_set_revert_to_history_rsp import ObjectSetRevertToHistoryRsp
from ecotaxa_py_client.model.object_set_summary_rsp import ObjectSetSummaryRsp
from ecotaxa_py_client.model.process_model import ProcessModel
from ecotaxa_py_client.model.project_filters import ProjectFilters
from ecotaxa_py_client.model.project_model import ProjectModel
from ecotaxa_py_client.model.project_summary_model import ProjectSummaryModel
from ecotaxa_py_client.model.project_taxo_stats_model import ProjectTaxoStatsModel
from ecotaxa_py_client.model.project_user_stats_model import ProjectUserStatsModel
from ecotaxa_py_client.model.sample_model import SampleModel
from ecotaxa_py_client.model.sample_taxo_stats_model import SampleTaxoStatsModel
from ecotaxa_py_client.model.simple_import_req import SimpleImportReq
from ecotaxa_py_client.model.simple_import_rsp import SimpleImportRsp
from ecotaxa_py_client.model.subset_req import SubsetReq
from ecotaxa_py_client.model.subset_rsp import SubsetRsp
from ecotaxa_py_client.model.taxa_search_rsp import TaxaSearchRsp
from ecotaxa_py_client.model.taxon_model import TaxonModel
from ecotaxa_py_client.model.taxon_usage_model import TaxonUsageModel
from ecotaxa_py_client.model.taxonomy_tree_status import TaxonomyTreeStatus
from ecotaxa_py_client.model.user_activity import UserActivity
from ecotaxa_py_client.model.user_model import UserModel
from ecotaxa_py_client.model.user_model_with_rights import UserModelWithRights
from ecotaxa_py_client.model.validation_error import ValidationError
