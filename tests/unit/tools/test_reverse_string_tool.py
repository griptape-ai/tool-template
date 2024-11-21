from griptape.artifacts import TextArtifact
from griptape.extension_name.tools.reverse_string import ReverseStringTool


class TestReverseStringTool:
    def test_reverse_string(self):
        value = "some_value"

        tool = ReverseStringTool()

        params = {"values": {"input": value}}
        result = tool.reverse_string(params)

        assert isinstance(result, TextArtifact), "Expected TextArtifact instance"
        assert result.value == value[::-1]
