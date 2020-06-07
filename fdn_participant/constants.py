from enum import Enum


class REVIEW_STATUS(Enum):
    NOT_REVIEWED = 'Not Reviewed'
    ACCEPTED = 'Reviewed - Accepted'
    NOT_ACCEPTED = 'Reviewed - Not Accepted'
