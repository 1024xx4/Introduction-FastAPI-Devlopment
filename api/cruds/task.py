from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.engine import Result, Row

import api.models.task as task_model
import api.schemas.task as task_schema


def get_task(db: Session, task_id: int) -> task_model.Task | None:
    result: Result = db.execute(
        select(task_model.Task).filter(task_model.Task.id == task_id)
    )
    return result.scalars().first()
    # scalars() で結果の各行から取得する要素を１つに絞り、値として抽出


def update_task(db: Session, task_create: task_schema.TaskCreate, original: task_model.Task) -> task_model.Task:
    original.title = task_create.title
    db.add(original)
    db.commit()
    db.refresh(original)
    return original


def get_task_with_done(db: Session) -> list[tuple[int, str, bool]]:
    result: Result = db.execute(  # イテレータとして定義
        select(
            task_model.Task.id,
            task_model.Task.title,
            task_model.Done.id.isnot(None).label("done"),  # Done.id が存在するときは done=True
        ).outerjoin(task_model.Done)
    )

    return result.all()  # すべての DB records を取得


def create_task(db: Session, task_create: task_schema.TaskCreate) -> task_model.Task:
    task = task_model.Task(**task_create.dict())  # task_schema.TaskCreate を task_model.Task に変換
    db.add(task)
    db.commit()  # DB に Commit
    db.refresh(task)  # DB条のデータをもとに task を更新する
    return task  # 作成した DBモデルを返す
