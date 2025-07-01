from typing import Type, Optional, get_type_hints
from pydantic import BaseModel, create_model

def partial_model(base_model: Type[BaseModel], model_name: str = None):
    hints = get_type_hints(base_model)
    fields = {
        name: (Optional[typ], None)
        for name, typ in hints.items()
    }
    return create_model(  # type: ignore
        model_name or f"Partial{base_model.__name__}",
        __base__=base_model,
        **fields
    )