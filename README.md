# Introduction-FastAPI-Devlopment
動かして学ぶ Python FastAPI 開発入門

## ToDo App の機能
REST に従う。

| 機能                       | REST API                     |
|--------------------------|------------------------------|
| ToDo List を表示する          | GET /tasks                   |
| ToDo に Task を追加する        | POST /tasks                  |
| ToDo の Task の説明文を変更する    | PUT /tasks/{task_id}         |
| ToDo の Task自体を削除する       | DELETE /tasks/{task_id}      |
| ToDo Task に「完了」flag を立てる | PUT /tasks/{task_id}/done    |
| ToDo Task から「完了」flag を外す | DELETE /tasks/{task_id}/done |