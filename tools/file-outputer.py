from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

import base64

class FileOutputerTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        content_base64 = tool_parameters.get("content_base64")
        output_filename = tool_parameters.get("output_filename") or "output.bin"
        mime_type = tool_parameters.get("mime_type") or "application/octet-stream"

        if not content_base64:
            yield self.create_text_message("content_base64 is required.")
            return

        # data URI 形式にも対応
        if "," in content_base64 and content_base64.strip().startswith("data:"):
            header, content_base64 = content_base64.split(",", 1)
            if ";base64" in header and header.startswith("data:"):
                detected_mime_type = header.removeprefix("data:").split(";")[0]
                if detected_mime_type:
                    mime_type = detected_mime_type

        try:
            output_bytes = base64.b64decode(content_base64, validate=True)
        except Exception as e:
            yield self.create_text_message(f"Invalid base64 content: {e}")
            return

        yield self.create_blob_message(
            blob=output_bytes,
            meta={
                "mime_type": mime_type,
                "filename": output_filename,
            },
        )

