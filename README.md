# ecotaxa_py_client
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.0.25
- Package version: 1.0.18
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/ecotaxa/ecotaxa_py_client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/ecotaxa/ecotaxa_py_client.git`)

Then import the package:
```python
import ecotaxa_py_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import ecotaxa_py_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import ecotaxa_py_client
from pprint import pprint
from ecotaxa_py_client.api import files_api
from ecotaxa_py_client.model.directory_model import DirectoryModel
from ecotaxa_py_client.model.http_validation_error import HTTPValidationError
 
from ecotaxa_py_client.api import authentification_api
from ecotaxa_py_client.model.login_req import LoginReq
# Defining the host is optional and defaults to https://ecotaxa.obs-vlfr.fr/api
# See configuration.py for a list of all supported configuration parameters.
configuration = ecotaxa_py_client.Configuration(
    host = "https://ecotaxa.obs-vlfr.fr/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization :
# You need to call the login api, [ https://github.com/ecotaxa/ecotaxa_py_client/blob/main/docs/AuthentificationApi.md#login | doc here ] .
# You should use your login and password from the ecotaxa webapp (if you are not registrated please sing up through [ https://ecotaxa.obs-vlfr.fr/login | this page ] ).
# This api call will return you a JWT token, you will use it as : YOUR_ACCESS_TOKEN for the following calls.

# Enter a context with an instance of the API client
with ecotaxa_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentification_api.AuthentificationApi(api_client)
    #setup your credentials
    login_req = LoginReq(
        password="yourPassword",
        username="your@email.com",
    ) # LoginReq | 

    # example passing only required values which don't have defaults set
    try:
        # Login
        api_response_token = api_instance.login(login_req)
        pprint(api_response)
        #set YOUR_ACCESS_TOKEN configuration
        configuration.access_token = api_response_token
    except ecotaxa_py_client.ApiException as e:
        print("Exception when calling AuthentificationApi->login: %s\n" % e)

    

# Enter a context with an instance of the API client
with ecotaxa_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = files_api.FilesApi(api_client)
    path = "/ftp_plankton/Ecotaxa_Exported_data" # str | 
    try:
        # List Common Files
        api_response = api_instance.list_common_files(path)
        pprint(api_response)
    except ecotaxa_py_client.ApiException as e:
        print("Exception when calling FilesApi->list_common_files: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://ecotaxa.obs-vlfr.fr/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*FilesApi* | [**list_common_files**](docs/FilesApi.md#list_common_files) | **GET** /common_files/ | List Common Files
*FilesApi* | [**list_user_files**](docs/FilesApi.md#list_user_files) | **GET** /my_files/{sub_path} | List User Files
*FilesApi* | [**post_user_file**](docs/FilesApi.md#post_user_file) | **POST** /my_files/ | Put User File
*TaxonomyTreeApi* | [**add_taxon_in_central**](docs/TaxonomyTreeApi.md#add_taxon_in_central) | **PUT** /taxon/central | Add Taxon In Central
*TaxonomyTreeApi* | [**get_taxon_in_central**](docs/TaxonomyTreeApi.md#get_taxon_in_central) | **GET** /taxon/central/{taxon_id} | Get Taxon In Central
*TaxonomyTreeApi* | [**pull_taxa_update_from_central**](docs/TaxonomyTreeApi.md#pull_taxa_update_from_central) | **GET** /taxa/pull_from_central | Pull Taxa Update From Central
*TaxonomyTreeApi* | [**push_taxa_stats_in_central**](docs/TaxonomyTreeApi.md#push_taxa_stats_in_central) | **GET** /taxa/stats/push_to_central | Push Taxa Stats In Central
*TaxonomyTreeApi* | [**query_root_taxa**](docs/TaxonomyTreeApi.md#query_root_taxa) | **GET** /taxa | Query Root Taxa
*TaxonomyTreeApi* | [**query_taxa**](docs/TaxonomyTreeApi.md#query_taxa) | **GET** /taxon/{taxon_id} | Query Taxa
*TaxonomyTreeApi* | [**query_taxa_set**](docs/TaxonomyTreeApi.md#query_taxa_set) | **GET** /taxon_set/query | Query Taxa Set
*TaxonomyTreeApi* | [**query_taxa_usage**](docs/TaxonomyTreeApi.md#query_taxa_usage) | **GET** /taxon/{taxon_id}/usage | Query Taxa Usage
*TaxonomyTreeApi* | [**reclassif_project_stats**](docs/TaxonomyTreeApi.md#reclassif_project_stats) | **GET** /taxa/reclassification_history/{project_id} | Reclassif Project Stats
*TaxonomyTreeApi* | [**reclassif_stats**](docs/TaxonomyTreeApi.md#reclassif_stats) | **GET** /taxa/reclassification_stats | Reclassif Stats
*TaxonomyTreeApi* | [**search_taxa**](docs/TaxonomyTreeApi.md#search_taxa) | **GET** /taxon_set/search | Search Taxa
*TaxonomyTreeApi* | [**taxa_tree_status**](docs/TaxonomyTreeApi.md#taxa_tree_status) | **GET** /taxa/status | Taxa Tree Status
*WIPApi* | [**system_status**](docs/WIPApi.md#system_status) | **GET** /status | System Status
*AcquisitionsApi* | [**acquisition_query**](docs/AcquisitionsApi.md#acquisition_query) | **GET** /acquisition/{acquisition_id} | Acquisition Query
*AcquisitionsApi* | [**acquisitions_search**](docs/AcquisitionsApi.md#acquisitions_search) | **GET** /acquisitions/search | Acquisitions Search
*AcquisitionsApi* | [**update_acquisitions**](docs/AcquisitionsApi.md#update_acquisitions) | **POST** /acquisition_set/update | Update Acquisitions
*AuthentificationApi* | [**login**](docs/AuthentificationApi.md#login) | **POST** /login | Login
*CollectionsApi* | [**collection_by_short_title**](docs/CollectionsApi.md#collection_by_short_title) | **GET** /collections/by_short_title | Collection By Short Title
*CollectionsApi* | [**collection_by_title**](docs/CollectionsApi.md#collection_by_title) | **GET** /collections/by_title | Collection By Title
*CollectionsApi* | [**create_collection**](docs/CollectionsApi.md#create_collection) | **POST** /collections/create | Create Collection
*CollectionsApi* | [**emodnet_format_export**](docs/CollectionsApi.md#emodnet_format_export) | **GET** /collections/{collection_id}/export/emodnet | Emodnet Format Export
*CollectionsApi* | [**erase_collection**](docs/CollectionsApi.md#erase_collection) | **DELETE** /collections/{collection_id} | Erase Collection
*CollectionsApi* | [**get_collection**](docs/CollectionsApi.md#get_collection) | **GET** /collections/{collection_id} | Get Collection
*CollectionsApi* | [**search_collections**](docs/CollectionsApi.md#search_collections) | **GET** /collections/search | Search Collections
*CollectionsApi* | [**update_collection**](docs/CollectionsApi.md#update_collection) | **PUT** /collections/{collection_id} | Update Collection
*InstrumentsApi* | [**instrument_query**](docs/InstrumentsApi.md#instrument_query) | **GET** /instruments/ | Instrument Query
*JobsApi* | [**erase_job**](docs/JobsApi.md#erase_job) | **DELETE** /jobs/{job_id} | Erase Job
*JobsApi* | [**get_job**](docs/JobsApi.md#get_job) | **GET** /jobs/{job_id}/ | Get Job
*JobsApi* | [**get_job_file**](docs/JobsApi.md#get_job_file) | **GET** /jobs/{job_id}/file | Get Job File
*JobsApi* | [**get_job_log_file**](docs/JobsApi.md#get_job_log_file) | **GET** /jobs/{job_id}/log | Get Job Log File
*JobsApi* | [**list_jobs**](docs/JobsApi.md#list_jobs) | **GET** /jobs/ | List Jobs
*JobsApi* | [**reply_job_question**](docs/JobsApi.md#reply_job_question) | **POST** /jobs/{job_id}/answer | Reply Job Question
*JobsApi* | [**restart_job**](docs/JobsApi.md#restart_job) | **GET** /jobs/{job_id}/restart | Restart Job
*MiscApi* | [**do_nothing**](docs/MiscApi.md#do_nothing) | **GET** /noop | Do Nothing
*MiscApi* | [**system_error**](docs/MiscApi.md#system_error) | **GET** /error | System Error
*MiscApi* | [**used_constants**](docs/MiscApi.md#used_constants) | **GET** /constants | Used Constants
*ObjectApi* | [**object_query**](docs/ObjectApi.md#object_query) | **GET** /object/{object_id} | Object Query
*ObjectApi* | [**object_query_history**](docs/ObjectApi.md#object_query_history) | **GET** /object/{object_id}/history | Object Query History
*ObjectsApi* | [**classify_auto_object_set**](docs/ObjectsApi.md#classify_auto_object_set) | **POST** /object_set/classify_auto | Classify Auto Object Set
*ObjectsApi* | [**classify_object_set**](docs/ObjectsApi.md#classify_object_set) | **POST** /object_set/classify | Classify Object Set
*ObjectsApi* | [**erase_object_set**](docs/ObjectsApi.md#erase_object_set) | **DELETE** /object_set/ | Erase Object Set
*ObjectsApi* | [**export_object_set**](docs/ObjectsApi.md#export_object_set) | **POST** /object_set/export | Export Object Set
*ObjectsApi* | [**get_object_set**](docs/ObjectsApi.md#get_object_set) | **POST** /object_set/{project_id}/query | Get Object Set
*ObjectsApi* | [**get_object_set_summary**](docs/ObjectsApi.md#get_object_set_summary) | **POST** /object_set/{project_id}/summary | Get Object Set Summary
*ObjectsApi* | [**predict_object_set**](docs/ObjectsApi.md#predict_object_set) | **POST** /object_set/predict | Predict Object Set
*ObjectsApi* | [**query_object_set_parents**](docs/ObjectsApi.md#query_object_set_parents) | **POST** /object_set/parents | Query Object Set Parents
*ObjectsApi* | [**reclassify_object_set**](docs/ObjectsApi.md#reclassify_object_set) | **POST** /object_set/{project_id}/reclassify | Reclassify Object Set
*ObjectsApi* | [**reset_object_set_to_predicted**](docs/ObjectsApi.md#reset_object_set_to_predicted) | **POST** /object_set/{project_id}/reset_to_predicted | Reset Object Set To Predicted
*ObjectsApi* | [**revert_object_set_to_history**](docs/ObjectsApi.md#revert_object_set_to_history) | **POST** /object_set/{project_id}/revert_to_history | Revert Object Set To History
*ObjectsApi* | [**update_object_set**](docs/ObjectsApi.md#update_object_set) | **POST** /object_set/update | Update Object Set
*ProcessesApi* | [**process_query**](docs/ProcessesApi.md#process_query) | **GET** /process/{process_id} | Process Query
*ProcessesApi* | [**update_processes**](docs/ProcessesApi.md#update_processes) | **POST** /process_set/update | Update Processes
*ProjectsApi* | [**create_project**](docs/ProjectsApi.md#create_project) | **POST** /projects/create | Create Project
*ProjectsApi* | [**erase_project**](docs/ProjectsApi.md#erase_project) | **DELETE** /projects/{project_id} | Erase Project
*ProjectsApi* | [**import_file**](docs/ProjectsApi.md#import_file) | **POST** /file_import/{project_id} | Import File
*ProjectsApi* | [**project_check**](docs/ProjectsApi.md#project_check) | **GET** /projects/{project_id}/check | Project Check
*ProjectsApi* | [**project_merge**](docs/ProjectsApi.md#project_merge) | **POST** /projects/{project_id}/merge | Project Merge
*ProjectsApi* | [**project_query**](docs/ProjectsApi.md#project_query) | **GET** /projects/{project_id} | Project Query
*ProjectsApi* | [**project_recompute_geography**](docs/ProjectsApi.md#project_recompute_geography) | **POST** /projects/{project_id}/recompute_geo | Project Recompute Geography
*ProjectsApi* | [**project_set_get_column_stats**](docs/ProjectsApi.md#project_set_get_column_stats) | **GET** /project_set/column_stats | Project Set Get Column Stats
*ProjectsApi* | [**project_set_get_stats**](docs/ProjectsApi.md#project_set_get_stats) | **GET** /project_set/taxo_stats | Project Set Get Stats
*ProjectsApi* | [**project_set_get_user_stats**](docs/ProjectsApi.md#project_set_get_user_stats) | **GET** /project_set/user_stats | Project Set Get User Stats
*ProjectsApi* | [**project_stats**](docs/ProjectsApi.md#project_stats) | **GET** /projects/{project_id}/stats | Project Stats
*ProjectsApi* | [**project_subset**](docs/ProjectsApi.md#project_subset) | **POST** /projects/{project_id}/subset | Project Subset
*ProjectsApi* | [**search_projects**](docs/ProjectsApi.md#search_projects) | **GET** /projects/search | Search Projects
*ProjectsApi* | [**set_project_predict_settings**](docs/ProjectsApi.md#set_project_predict_settings) | **PUT** /projects/{project_id}/prediction_settings | Set Project Predict Settings
*ProjectsApi* | [**simple_import**](docs/ProjectsApi.md#simple_import) | **POST** /simple_import/{project_id} | Simple Import
*ProjectsApi* | [**update_project**](docs/ProjectsApi.md#update_project) | **PUT** /projects/{project_id} | Update Project
*SamplesApi* | [**sample_query**](docs/SamplesApi.md#sample_query) | **GET** /sample/{sample_id} | Sample Query
*SamplesApi* | [**sample_set_get_stats**](docs/SamplesApi.md#sample_set_get_stats) | **GET** /sample_set/taxo_stats | Sample Set Get Stats
*SamplesApi* | [**samples_search**](docs/SamplesApi.md#samples_search) | **GET** /samples/search | Samples Search
*SamplesApi* | [**update_samples**](docs/SamplesApi.md#update_samples) | **POST** /sample_set/update | Update Samples
*UsersApi* | [**get_current_user_prefs**](docs/UsersApi.md#get_current_user_prefs) | **GET** /users/my_preferences/{project_id} | Get Current User Prefs
*UsersApi* | [**get_user**](docs/UsersApi.md#get_user) | **GET** /users/{user_id} | Get User
*UsersApi* | [**get_users**](docs/UsersApi.md#get_users) | **GET** /users | Get Users
*UsersApi* | [**get_users_admins**](docs/UsersApi.md#get_users_admins) | **GET** /users/admins | Get Users Admins
*UsersApi* | [**search_user**](docs/UsersApi.md#search_user) | **GET** /users/search | Search User
*UsersApi* | [**set_current_user_prefs**](docs/UsersApi.md#set_current_user_prefs) | **PUT** /users/my_preferences/{project_id} | Set Current User Prefs
*UsersApi* | [**show_current_user**](docs/UsersApi.md#show_current_user) | **GET** /users/me | Show Current User


## Documentation For Models

 - [AcquisitionModel](docs/AcquisitionModel.md)
 - [BodyExportObjectSetObjectSetExportPost](docs/BodyExportObjectSetObjectSetExportPost.md)
 - [BodyPredictObjectSetObjectSetPredictPost](docs/BodyPredictObjectSetObjectSetPredictPost.md)
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
 - [PredictionReq](docs/PredictionReq.md)
 - [PredictionRsp](docs/PredictionRsp.md)
 - [ProcessModel](docs/ProcessModel.md)
 - [ProjectFilters](docs/ProjectFilters.md)
 - [ProjectModel](docs/ProjectModel.md)
 - [ProjectSetColumnStatsModel](docs/ProjectSetColumnStatsModel.md)
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
 - [TaxonCentral](docs/TaxonCentral.md)
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




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in ecotaxa_py_client.apis and ecotaxa_py_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from ecotaxa_py_client.api.default_api import DefaultApi`
- `from ecotaxa_py_client.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import ecotaxa_py_client
from ecotaxa_py_client.apis import *
from ecotaxa_py_client.models import *
```

