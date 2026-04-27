from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.api_error import APIError
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, Optional


@dataclass
class ListarCertificados5XXError(APIError):
    additional_data: Dict[str, Any] = field(default_factory=dict)

    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ListarCertificados5XXError:
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ListarCertificados5XXError()

    def get_field_deserializers(self) -> Dict[str, Callable[[ParseNode], None]]:
        return {}

    def serialize(self, writer: SerializationWriter) -> None:
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_additional_data_value(self.additional_data)

    @property
    def primary_message(self) -> str:
        return super().message
