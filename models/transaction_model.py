from dataclasses import dataclass
from typing import Optional
from enum import Enum

class TransactionType(Enum):
    CREDIT = "credit"
    DEBIT = "debit"

@dataclass
class Amount:
    value: float
    currency: str

@dataclass
class TransactionMetadata:
    order_id: str
    customer_reference: str

@dataclass
class Transaction:
    reference: str
    amount: Amount
    description: str
    metadata: TransactionMetadata
    transaction_type: TransactionType 