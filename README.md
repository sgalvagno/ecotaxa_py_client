# ecotaxa-cli-py
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.0.17
- Package version: 1.0.5
- Build package: org.openapitools.codegen.languages.PythonLegacyClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import ecotaxa_cli_py
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import ecotaxa_cli_py
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function

import time
import ecotaxa_cli_py
from ecotaxa_cli_py.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://ecotaxa.obs-vlfr.fr/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ecotaxa_cli_py.Configuration(
    host = "https://ecotaxa.obs-vlfr.fr/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: BearerOrCookieAuth
configuration = ecotaxa_cli_py.Configuration(
    host = "https://ecotaxa.obs-vlfr.fr/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


# Enter a context with an instance of the API client
with ecotaxa_cli_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ecotaxa_cli_py.FilesApi(api_client)
    path = 'path_example' # str | 

    try:
        # List Common Files
        api_response = api_instance.list_common_files_common_files_get(path)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->list_common_files_common_files_get: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *https://ecotaxa.obs-vlfr.fr/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*FilesApi* | [**list_common_files_common_files_get**](docs/FilesApi.md#list_common_files_common_files_get) | **GET** /common_files/ | List Common Files
*FilesApi* | [**list_user_files_my_files_sub_path_get**](docs/FilesApi.md#list_user_files_my_files_sub_path_get) | **GET** /my_files/{sub_path} | List User Files
*FilesApi* | [**put_user_file_my_files_post**](docs/FilesApi.md#put_user_file_my_files_post) | **POST** /my_files/ | Put User File
*TaxonomyTreeApi* | [**add_taxon_in_central_taxon_central_put**](docs/TaxonomyTreeApi.md#add_taxon_in_central_taxon_central_put) | **PUT** /taxon/central | Add Taxon In Central
*TaxonomyTreeApi* | [**get_taxon_in_central_taxon_central_taxon_id_get**](docs/TaxonomyTreeApi.md#get_taxon_in_central_taxon_central_taxon_id_get) | **GET** /taxon/central/{taxon_id} | Get Taxon In Central
*TaxonomyTreeApi* | [**pull_taxa_update_from_central_taxa_pull_from_central_get**](docs/TaxonomyTreeApi.md#pull_taxa_update_from_central_taxa_pull_from_central_get) | **GET** /taxa/pull_from_central | Pull Taxa Update From Central
*TaxonomyTreeApi* | [**push_taxa_stats_in_central_taxa_stats_push_to_central_get**](docs/TaxonomyTreeApi.md#push_taxa_stats_in_central_taxa_stats_push_to_central_get) | **GET** /taxa/stats/push_to_central | Push Taxa Stats In Central
*TaxonomyTreeApi* | [**query_root_taxa_taxa_get**](docs/TaxonomyTreeApi.md#query_root_taxa_taxa_get) | **GET** /taxa | Query Root Taxa
*TaxonomyTreeApi* | [**query_taxa_set_taxon_set_query_get**](docs/TaxonomyTreeApi.md#query_taxa_set_taxon_set_query_get) | **GET** /taxon_set/query | Query Taxa Set
*TaxonomyTreeApi* | [**query_taxa_taxon_taxon_id_get**](docs/TaxonomyTreeApi.md#query_taxa_taxon_taxon_id_get) | **GET** /taxon/{taxon_id} | Query Taxa
*TaxonomyTreeApi* | [**query_taxa_usage_taxon_taxon_id_usage_get**](docs/TaxonomyTreeApi.md#query_taxa_usage_taxon_taxon_id_usage_get) | **GET** /taxon/{taxon_id}/usage | Query Taxa Usage
*TaxonomyTreeApi* | [**reclassif_project_stats_taxa_reclassification_history_project_id_get**](docs/TaxonomyTreeApi.md#reclassif_project_stats_taxa_reclassification_history_project_id_get) | **GET** /taxa/reclassification_history/{project_id} | Reclassif Project Stats
*TaxonomyTreeApi* | [**reclassif_stats_taxa_reclassification_stats_get**](docs/TaxonomyTreeApi.md#reclassif_stats_taxa_reclassification_stats_get) | **GET** /taxa/reclassification_stats | Reclassif Stats
*TaxonomyTreeApi* | [**search_taxa_taxon_set_search_get**](docs/TaxonomyTreeApi.md#search_taxa_taxon_set_search_get) | **GET** /taxon_set/search | Search Taxa
*TaxonomyTreeApi* | [**taxa_tree_status_taxa_status_get**](docs/TaxonomyTreeApi.md#taxa_tree_status_taxa_status_get) | **GET** /taxa/status | Taxa Tree Status
*WIPApi* | [**system_status_status_get**](docs/WIPApi.md#system_status_status_get) | **GET** /status | System Status
*AcquisitionsApi* | [**acquisition_query_acquisition_acquisition_id_get**](docs/AcquisitionsApi.md#acquisition_query_acquisition_acquisition_id_get) | **GET** /acquisition/{acquisition_id} | Acquisition Query
*AcquisitionsApi* | [**acquisitions_search_acquisitions_search_get**](docs/AcquisitionsApi.md#acquisitions_search_acquisitions_search_get) | **GET** /acquisitions/search | Acquisitions Search
*AcquisitionsApi* | [**update_acquisitions_acquisition_set_update_post**](docs/AcquisitionsApi.md#update_acquisitions_acquisition_set_update_post) | **POST** /acquisition_set/update | Update Acquisitions
*AuthentificationApi* | [**login_login_post**](docs/AuthentificationApi.md#login_login_post) | **POST** /login | Login
*CollectionsApi* | [**collection_by_short_title_collections_by_short_title_get**](docs/CollectionsApi.md#collection_by_short_title_collections_by_short_title_get) | **GET** /collections/by_short_title | Collection By Short Title
*CollectionsApi* | [**collection_by_title_collections_by_title_get**](docs/CollectionsApi.md#collection_by_title_collections_by_title_get) | **GET** /collections/by_title | Collection By Title
*CollectionsApi* | [**create_collection_collections_create_post**](docs/CollectionsApi.md#create_collection_collections_create_post) | **POST** /collections/create | Create Collection
*CollectionsApi* | [**emodnet_format_export_collections_collection_id_export_emodnet_get**](docs/CollectionsApi.md#emodnet_format_export_collections_collection_id_export_emodnet_get) | **GET** /collections/{collection_id}/export/emodnet | Emodnet Format Export
*CollectionsApi* | [**erase_collection_collections_collection_id_delete**](docs/CollectionsApi.md#erase_collection_collections_collection_id_delete) | **DELETE** /collections/{collection_id} | Erase Collection
*CollectionsApi* | [**get_collection_collections_collection_id_get**](docs/CollectionsApi.md#get_collection_collections_collection_id_get) | **GET** /collections/{collection_id} | Get Collection
*CollectionsApi* | [**search_collections_collections_search_get**](docs/CollectionsApi.md#search_collections_collections_search_get) | **GET** /collections/search | Search Collections
*CollectionsApi* | [**update_collection_collections_collection_id_put**](docs/CollectionsApi.md#update_collection_collections_collection_id_put) | **PUT** /collections/{collection_id} | Update Collection
*InstrumentApi* | [**instrument_query_instruments_get**](docs/InstrumentApi.md#instrument_query_instruments_get) | **GET** /instruments/ | Instrument Query
*JobsApi* | [**erase_job_jobs_job_id_delete**](docs/JobsApi.md#erase_job_jobs_job_id_delete) | **DELETE** /jobs/{job_id} | Erase Job
*JobsApi* | [**get_job_file_jobs_job_id_file_get**](docs/JobsApi.md#get_job_file_jobs_job_id_file_get) | **GET** /jobs/{job_id}/file | Get Job File
*JobsApi* | [**get_job_jobs_job_id_get**](docs/JobsApi.md#get_job_jobs_job_id_get) | **GET** /jobs/{job_id}/ | Get Job
*JobsApi* | [**get_job_log_file_jobs_job_id_log_get**](docs/JobsApi.md#get_job_log_file_jobs_job_id_log_get) | **GET** /jobs/{job_id}/log | Get Job Log File
*JobsApi* | [**list_jobs_jobs_get**](docs/JobsApi.md#list_jobs_jobs_get) | **GET** /jobs/ | List Jobs
*JobsApi* | [**reply_job_question_jobs_job_id_answer_post**](docs/JobsApi.md#reply_job_question_jobs_job_id_answer_post) | **POST** /jobs/{job_id}/answer | Reply Job Question
*JobsApi* | [**restart_job_jobs_job_id_restart_get**](docs/JobsApi.md#restart_job_jobs_job_id_restart_get) | **GET** /jobs/{job_id}/restart | Restart Job
*MiscApi* | [**do_nothing_noop_get**](docs/MiscApi.md#do_nothing_noop_get) | **GET** /noop | Do Nothing
*MiscApi* | [**system_error_error_get**](docs/MiscApi.md#system_error_error_get) | **GET** /error | System Error
*MiscApi* | [**used_constants_constants_get**](docs/MiscApi.md#used_constants_constants_get) | **GET** /constants | Used Constants
*ObjectApi* | [**object_query_history_object_object_id_history_get**](docs/ObjectApi.md#object_query_history_object_object_id_history_get) | **GET** /object/{object_id}/history | Object Query History
*ObjectApi* | [**object_query_object_object_id_get**](docs/ObjectApi.md#object_query_object_object_id_get) | **GET** /object/{object_id} | Object Query
*ObjectsApi* | [**classify_auto_object_set_object_set_classify_auto_post**](docs/ObjectsApi.md#classify_auto_object_set_object_set_classify_auto_post) | **POST** /object_set/classify_auto | Classify Auto Object Set
*ObjectsApi* | [**classify_object_set_object_set_classify_post**](docs/ObjectsApi.md#classify_object_set_object_set_classify_post) | **POST** /object_set/classify | Classify Object Set
*ObjectsApi* | [**erase_object_set_object_set_delete**](docs/ObjectsApi.md#erase_object_set_object_set_delete) | **DELETE** /object_set/ | Erase Object Set
*ObjectsApi* | [**export_object_set_object_set_export_post**](docs/ObjectsApi.md#export_object_set_object_set_export_post) | **POST** /object_set/export | Export Object Set
*ObjectsApi* | [**get_object_set_object_set_project_id_query_post**](docs/ObjectsApi.md#get_object_set_object_set_project_id_query_post) | **POST** /object_set/{project_id}/query | Get Object Set
*ObjectsApi* | [**get_object_set_summary_object_set_project_id_summary_post**](docs/ObjectsApi.md#get_object_set_summary_object_set_project_id_summary_post) | **POST** /object_set/{project_id}/summary | Get Object Set Summary
*ObjectsApi* | [**query_object_set_parents_object_set_parents_post**](docs/ObjectsApi.md#query_object_set_parents_object_set_parents_post) | **POST** /object_set/parents | Query Object Set Parents
*ObjectsApi* | [**reclassify_object_set_object_set_project_id_reclassify_post**](docs/ObjectsApi.md#reclassify_object_set_object_set_project_id_reclassify_post) | **POST** /object_set/{project_id}/reclassify | Reclassify Object Set
*ObjectsApi* | [**reset_object_set_to_predicted_object_set_project_id_reset_to_predicted_post**](docs/ObjectsApi.md#reset_object_set_to_predicted_object_set_project_id_reset_to_predicted_post) | **POST** /object_set/{project_id}/reset_to_predicted | Reset Object Set To Predicted
*ObjectsApi* | [**revert_object_set_to_history_object_set_project_id_revert_to_history_post**](docs/ObjectsApi.md#revert_object_set_to_history_object_set_project_id_revert_to_history_post) | **POST** /object_set/{project_id}/revert_to_history | Revert Object Set To History
*ObjectsApi* | [**update_object_set_object_set_update_post**](docs/ObjectsApi.md#update_object_set_object_set_update_post) | **POST** /object_set/update | Update Object Set
*ProcessesApi* | [**process_query_process_process_id_get**](docs/ProcessesApi.md#process_query_process_process_id_get) | **GET** /process/{process_id} | Process Query
*ProcessesApi* | [**update_processes_process_set_update_post**](docs/ProcessesApi.md#update_processes_process_set_update_post) | **POST** /process_set/update | Update Processes
*ProjectsApi* | [**create_project_projects_create_post**](docs/ProjectsApi.md#create_project_projects_create_post) | **POST** /projects/create | Create Project
*ProjectsApi* | [**erase_project_projects_project_id_delete**](docs/ProjectsApi.md#erase_project_projects_project_id_delete) | **DELETE** /projects/{project_id} | Erase Project
*ProjectsApi* | [**import_file_file_import_project_id_post**](docs/ProjectsApi.md#import_file_file_import_project_id_post) | **POST** /file_import/{project_id} | Import File
*ProjectsApi* | [**project_check_projects_project_id_check_get**](docs/ProjectsApi.md#project_check_projects_project_id_check_get) | **GET** /projects/{project_id}/check | Project Check
*ProjectsApi* | [**project_merge_projects_project_id_merge_post**](docs/ProjectsApi.md#project_merge_projects_project_id_merge_post) | **POST** /projects/{project_id}/merge | Project Merge
*ProjectsApi* | [**project_query_projects_project_id_get**](docs/ProjectsApi.md#project_query_projects_project_id_get) | **GET** /projects/{project_id} | Project Query
*ProjectsApi* | [**project_recompute_geography_projects_project_id_recompute_geo_post**](docs/ProjectsApi.md#project_recompute_geography_projects_project_id_recompute_geo_post) | **POST** /projects/{project_id}/recompute_geo | Project Recompute Geography
*ProjectsApi* | [**project_set_get_stats_project_set_taxo_stats_get**](docs/ProjectsApi.md#project_set_get_stats_project_set_taxo_stats_get) | **GET** /project_set/taxo_stats | Project Set Get Stats
*ProjectsApi* | [**project_set_get_user_stats_project_set_user_stats_get**](docs/ProjectsApi.md#project_set_get_user_stats_project_set_user_stats_get) | **GET** /project_set/user_stats | Project Set Get User Stats
*ProjectsApi* | [**project_stats_projects_project_id_stats_get**](docs/ProjectsApi.md#project_stats_projects_project_id_stats_get) | **GET** /projects/{project_id}/stats | Project Stats
*ProjectsApi* | [**project_subset_projects_project_id_subset_post**](docs/ProjectsApi.md#project_subset_projects_project_id_subset_post) | **POST** /projects/{project_id}/subset | Project Subset
*ProjectsApi* | [**search_projects_projects_search_get**](docs/ProjectsApi.md#search_projects_projects_search_get) | **GET** /projects/search | Search Projects
*ProjectsApi* | [**simple_import_simple_import_project_id_post**](docs/ProjectsApi.md#simple_import_simple_import_project_id_post) | **POST** /simple_import/{project_id} | Simple Import
*ProjectsApi* | [**update_project_projects_project_id_put**](docs/ProjectsApi.md#update_project_projects_project_id_put) | **PUT** /projects/{project_id} | Update Project
*SamplesApi* | [**sample_query_sample_sample_id_get**](docs/SamplesApi.md#sample_query_sample_sample_id_get) | **GET** /sample/{sample_id} | Sample Query
*SamplesApi* | [**sample_set_get_stats_sample_set_taxo_stats_get**](docs/SamplesApi.md#sample_set_get_stats_sample_set_taxo_stats_get) | **GET** /sample_set/taxo_stats | Sample Set Get Stats
*SamplesApi* | [**samples_search_samples_search_get**](docs/SamplesApi.md#samples_search_samples_search_get) | **GET** /samples/search | Samples Search
*SamplesApi* | [**update_samples_sample_set_update_post**](docs/SamplesApi.md#update_samples_sample_set_update_post) | **POST** /sample_set/update | Update Samples
*UsersApi* | [**get_current_user_prefs_users_my_preferences_project_id_get**](docs/UsersApi.md#get_current_user_prefs_users_my_preferences_project_id_get) | **GET** /users/my_preferences/{project_id} | Get Current User Prefs
*UsersApi* | [**get_user_users_user_id_get**](docs/UsersApi.md#get_user_users_user_id_get) | **GET** /users/{user_id} | Get User
*UsersApi* | [**get_users_users_get**](docs/UsersApi.md#get_users_users_get) | **GET** /users | Get Users
*UsersApi* | [**search_user_users_search_get**](docs/UsersApi.md#search_user_users_search_get) | **GET** /users/search | Search User
*UsersApi* | [**set_current_user_prefs_users_my_preferences_project_id_put**](docs/UsersApi.md#set_current_user_prefs_users_my_preferences_project_id_put) | **PUT** /users/my_preferences/{project_id} | Set Current User Prefs
*UsersApi* | [**show_current_user_users_me_get**](docs/UsersApi.md#show_current_user_users_me_get) | **GET** /users/me | Show Current User


## Documentation For Models

 - [AcquisitionModel](docs/AcquisitionModel.md)
 - [BodyExportObjectSetObjectSetExportPost](docs/BodyExportObjectSetObjectSetExportPost.md)
 - [BulkUpdateReq](docs/BulkUpdateReq.md)
 - [ClassifyAutoReq](docs/ClassifyAutoReq.md)
 - [ClassifyReq](docs/ClassifyReq.md)
 - [CollectionModel](docs/CollectionModel.md)
 - [Constants](docs/Constants.md)
 - [CreateCollectionReq](docs/CreateCollectionReq.md)
 - [CreateProjectReq](docs/CreateProjectReq.md)
 - [DirectoryEntryModel](docs/DirectoryEntryModel.md)
 - [DirectoryModel](docs/DirectoryModel.md)
 - [EMODnetExportRsp](docs/EMODnetExportRsp.md)
 - [ExportReq](docs/ExportReq.md)
 - [ExportRsp](docs/ExportRsp.md)
 - [ExportTypeEnum](docs/ExportTypeEnum.md)
 - [GroupDefinitions](docs/GroupDefinitions.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [HistoricalClassification](docs/HistoricalClassification.md)
 - [HistoricalLastClassif](docs/HistoricalLastClassif.md)
 - [ImageModel](docs/ImageModel.md)
 - [ImportReq](docs/ImportReq.md)
 - [ImportRsp](docs/ImportRsp.md)
 - [JobModel](docs/JobModel.md)
 - [LimitMethods](docs/LimitMethods.md)
 - [LoginReq](docs/LoginReq.md)
 - [MergeRsp](docs/MergeRsp.md)
 - [MinimalUserBO](docs/MinimalUserBO.md)
 - [ObjectHeaderModel](docs/ObjectHeaderModel.md)
 - [ObjectModel](docs/ObjectModel.md)
 - [ObjectSetQueryRsp](docs/ObjectSetQueryRsp.md)
 - [ObjectSetRevertToHistoryRsp](docs/ObjectSetRevertToHistoryRsp.md)
 - [ObjectSetSummaryRsp](docs/ObjectSetSummaryRsp.md)
 - [ProcessModel](docs/ProcessModel.md)
 - [ProjectFilters](docs/ProjectFilters.md)
 - [ProjectModel](docs/ProjectModel.md)
 - [ProjectSummaryModel](docs/ProjectSummaryModel.md)
 - [ProjectTaxoStatsModel](docs/ProjectTaxoStatsModel.md)
 - [ProjectUserStatsModel](docs/ProjectUserStatsModel.md)
 - [SampleModel](docs/SampleModel.md)
 - [SampleTaxoStatsModel](docs/SampleTaxoStatsModel.md)
 - [SimpleImportReq](docs/SimpleImportReq.md)
 - [SimpleImportRsp](docs/SimpleImportRsp.md)
 - [SubsetReq](docs/SubsetReq.md)
 - [SubsetRsp](docs/SubsetRsp.md)
 - [TaxaSearchRsp](docs/TaxaSearchRsp.md)
 - [TaxonModel](docs/TaxonModel.md)
 - [TaxonUsageModel](docs/TaxonUsageModel.md)
 - [TaxonomyTreeStatus](docs/TaxonomyTreeStatus.md)
 - [UserActivity](docs/UserActivity.md)
 - [UserModel](docs/UserModel.md)
 - [UserModelWithRights](docs/UserModelWithRights.md)
 - [ValidationError](docs/ValidationError.md)


## Documentation For Authorization


## BearerOrCookieAuth

- **Type**: OAuth
- **Flow**: password
- **Authorization URL**: 
- **Scopes**: N/A


## Author




