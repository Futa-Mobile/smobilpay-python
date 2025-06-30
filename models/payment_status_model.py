from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class PaymentStatusModel:
    ptn: str
    serviceid: str
    merchant: str
    timestamp: Optional[datetime]
    receiptNumber: str
    veriCode: str
    clearingDate: Optional[datetime]
    trid: str
    priceLocalCur: float
    priceSystemCur: float
    localCur: str
    systemCur: str
    pin: str
    status: str
    payItemId: str
    payItemDescr: str
    errorCode: int
    tag: str
