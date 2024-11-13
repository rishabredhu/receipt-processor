from typing import Dict, Optional
from app.api.schemas import Receipt
import uuid

class MemoryStore:
    def __init__(self):
        self._store: Dict[str, Receipt] = {}

    def save_receipt(self, receipt: Receipt) -> str:
        #generate a unique id for the receipt
        receipt_id = str(uuid.uuid4())

        #store receipt in dictionary using ID as key
        self._store[receipt_id] = receipt
        return receipt_id

    def get_receipt(self, receipt_id: str) -> Optional[Receipt]:
        return self._store.get(receipt_id)

# Global store instance
store = MemoryStore()