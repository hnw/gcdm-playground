[deploymentmanager-samples/examples/v2/cloud_functions](https://github.com/GoogleCloudPlatform/deploymentmanager-samples/tree/master/examples/v2/cloud_functions) で提供されているCloud Functions用のテンプレートをPython対応させたもの。

## 実験方法

```
$ gcloud deployment-manager deployments create [deploy名] --config cloud_function.yaml
```

## ログ

```
$ gcloud deployment-manager deployments create deploy-function --config cloud_function.yaml
The fingerprint of the deployment is h9MhJKWxN1DoQaf-6mJ6Iw==
The fingerprint of the deployment is h9MhJKWxN1DoQaf-6mJ6Iw==
Waiting for create [operation-1542572767433-57af635d7d12a-80d6041d-c04dffd6]...done.
Create operation operation-1542572767433-57af635d7d12a-80d6041d-c04dffd6 completed successfully.
NAME                  TYPE                                                                        STATE      ERRORS  INTENT
create-bucket         gcp-types/storage-v1:buckets                                                COMPLETED  []
create-function       gcp-types/cloudfunctions-v1:projects.locations.functions                    COMPLETED  []
function-call         gcp-types/cloudfunctions-v1:cloudfunctions.projects.locations.functions.ca  COMPLETED  []
                      ll
upload-function-code  gcp-types/cloudbuild-v1:cloudbuild.projects.builds.create                   COMPLETED  []
OUTPUTS          VALUE
bucket-name      bucket-deploy-function
function-output  Hello, World!
```
