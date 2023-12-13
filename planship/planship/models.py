from datetime import datetime
from typing import Any, Dict, Optional

from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class ModifySubscriptionParameters(BaseModel):
    plan_slug: Optional[StrictStr]
    renew_plan_slug: Optional[StrictStr]
    max_subscribers: Optional[StrictInt]
    auto_renew: Optional[StrictBool]
    is_active: Optional[StrictBool]
    renew_at: Optional[datetime]


class CreateSubscriptionParameters(BaseModel):
    is_subscriber: Optional[StrictBool] = True
    max_subscribers: Optional[StrictInt]
    auto_renew: Optional[StrictBool]
    renew_at: Optional[datetime]
    metadata: Optional[Dict[str, Any]] = None


class CreateCustomerParameters(BaseModel):
    metadata: Optional[Dict[str, Any]] = None
    name: Optional[StrictStr] = ""
    email: Optional[StrictStr] = ""
    alternative_id: Optional[StrictStr] = None
