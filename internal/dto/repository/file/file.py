from typing import Protocol
from uuid import UUID

import pandas as pd

from internal.dto.repository.base_schema import (
    BaseCreateSchema,
    BaseUpdateSchema,
    BaseSchema,
)


class File(Protocol):

    filename: str | None
    content_type: str | None

    async def read(self, chunk_size: int) -> bytes: ...


class FileBaseSchema(BaseSchema):
    file_name: UUID


class FileCreateSchema(FileBaseSchema, BaseCreateSchema): ...


class FileUpdateSchema(FileBaseSchema, BaseUpdateSchema): ...


class FileFindSchema(FileBaseSchema, BaseSchema): ...  # it's not a typo


FileResponseSchema = None


class CSVFileFindSchema(FileFindSchema):
    separator: str
    header: list[int]


CSVFileResponseSchema = pd.DataFrame


class FailedFileReadingException(Exception):
    """
    Exception raised when file reading fails.

    This exception can be used to provide specific error messages
    related to file reading operations in repository.
    """

    def __init__(self, message: str):
        """
        Initializes an instance of FailedFileReadingException with a specific error message.

        Args:
            message(str): The error message to be reported.
        """
        super().__init__(message)
