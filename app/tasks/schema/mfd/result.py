from app.tasks.schema.specific_with_deps_result import SpecificTaskWithDepsResult


class MFDTaskResult(SpecificTaskWithDepsResult):
    is_holding: bool | None
