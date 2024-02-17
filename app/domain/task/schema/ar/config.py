from typing import Annotated
from pydantic import Field
from app.domain.task.schema.base_config import BaseTaskConfig


class ARTaskConfig(BaseTaskConfig):
    min_support_ar: Annotated[float, Field(ge=0, le=1)]
    min_confidence: Annotated[float, Field(ge=0, le=1)]
