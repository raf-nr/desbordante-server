from app.domain.task.schema.specific_with_deps_result import SpecificTaskWithDepsResult


class ARTaskResult(SpecificTaskWithDepsResult):
    value_dictionary: dict[int, int] | None
