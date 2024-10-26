from abc import ABC, abstractmethod
from typing import Dict, List, Any


class IBlock(ABC):
    """Provides an interface to interact with blocks."""

    @abstractmethod
    def process_data(schema: Dict[str, Any], data: List[Any]):
        pass
