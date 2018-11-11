テンプレートのoutputを別のテンプレートのpropertiesに入れる実験。

具体的には、Pub/Subトピックを作るテンプレートがトピック名を返し、Pub/Subサブスクライバを作るテンプレートに渡すような設定を書いている。

## 実験方法

```
$ gcloud deployment-manager deployments create [deploy名] --config create_pubsub.yaml
```

## ログ

```
$ gcloud deployment-manager deployments create dpl-pubsub --config create_pubsub.yaml
The fingerprint of the deployment is cLuoNs8FA3bEzOzsmNG6aw==
Waiting for update [operation-1541932646216-57a612ba53141-ef58ab0b-556ed27a]...done.
Update operation operation-1541932646216-57a612ba53141-ef58ab0b-556ed27a completed successfully.
NAME                 TYPE                                        STATE      ERRORS  INTENT
create-subscription  gcp-types/pubsub-v1:projects.subscriptions  COMPLETED  []
create-topic         gcp-types/pubsub-v1:projects.topics         COMPLETED  []
OUTPUTS            VALUE
topic-name         projects/gce-hnw/topics/dpl-pubsub-my-topic
subscription-name  projects/gce-hnw/subscriptions/dpl-pubsub-my-subscription
```
