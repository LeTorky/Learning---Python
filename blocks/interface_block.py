from abc import ABC
from typing import Dict, List, Any


class IBlock(ABC):
    
    def process_data(schema: Dict[str, Any], data: List[Any]):
        pass
