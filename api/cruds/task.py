from sqlalchemy.orm import Session

import api.models.task as task_model
import api.schemas.task as task_schema


def create_task(db: Session, task_create: task_schema.TaskCreate) -> task_model.Task:
    task = task_model.Task(**task_create.dict())  # task_schema.TaskCreate を task_model.Task に変換
    db.add(task)
    db.commit()  # DB に Commit
    db.refresh(task)  # DB条のデータをもとに task を更新する
    return task  # 作成した DBモデルを返す
