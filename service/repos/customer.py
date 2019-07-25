from .base import BaseRepository
from ..models import Customer


class CustomerRepository(BaseRepository):

    _model = Customer
