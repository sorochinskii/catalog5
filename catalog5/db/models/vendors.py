from sqlalchemy.orm import Mapped, mapped_column

from catalog5.db.models.base import BaseCommon


class Vendor(BaseCommon):
    name: Mapped[str] = mapped_column(unique=True, index=True)
