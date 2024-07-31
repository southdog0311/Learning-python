from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class OnlineCourse(BaseModel):
    title: str
    description: str
    instructor: str
    start_date: date
    end_date: Optional[date]
    topics: List[str]
    price: float


course = OnlineCourse(
    title="Python Programming for Beginners",
    description="An introductory course to Python programming.",
    instructor="southdog",
    start_date=date(2024, 7, 10),
    end_date=None,
    topics=["Python Basics", "Data Structures", "Functions", "Modules"],
    price=5000
)

print(course)
