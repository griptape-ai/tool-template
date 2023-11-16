from __future__ import annotations
from griptape.artifacts import TextArtifact, ErrorArtifact
from griptape.tools import BaseTool
from griptape.utils.decorators import activity
from schema import Schema, Literal
from attr import define


@define
class ReverseStringTool(BaseTool):
    @activity(
        config={
            "description": "Can be used to reverse a string",
            "schema": Schema({Literal("input", description="The string to be reversed"): str}),
        }
    )
    def reverse_string(self, params: dict) -> TextArtifact | ErrorArtifact:
        input_value = params["values"].get("input")

        try:
            return TextArtifact(input_value[::-1])

        except Exception as e:
            return ErrorArtifact(str(e))
