import pytest
from pydantic import BaseModel, ValidationError
from datetime import date
from typing import List, Optional

# 定義 OnlineCourse 類別
class OnlineCourse(BaseModel):
    title: str
    description: str
    instructor: str
    start_date: date
    end_date: Optional[date]
    topics: List[str]
    price: float

def test_online_course_creation():
    # 測試有效的 OnlineCourse 創建
    course = OnlineCourse(
        title="Python Programming for Beginners",
        description="An introductory course to Python programming.",
        instructor="southdog",
        start_date=date(2024, 7, 10),
        end_date=None,
        topics=["Python Basics", "Data Structures", "Functions", "Modules"],
        price=5000
    )
    assert course.title == "Python Programming for Beginners"
    assert course.description == "An introductory course to Python programming."
    assert course.instructor == "southdog"
    assert course.start_date == date(2024, 7, 10)
    assert course.end_date is None
    assert course.topics == ["Python Basics", "Data Structures", "Functions", "Modules"]
    assert course.price == 5000

def test_online_course_invalid_price():
    # 測試無效的價格
    with pytest.raises(ValidationError):
        OnlineCourse(
            title="Python Programming for Beginners",
            description="An introductory course to Python programming.",
            instructor="southdog",
            start_date=date(2024, 7, 10),
            end_date=None,
            topics=["Python Basics", "Data Structures", "Functions", "Modules"],
            price="invalid_price"
        )

def test_online_course_missing_title():
    # 測試缺少標題
    with pytest.raises(ValidationError):
        OnlineCourse(
            description="An introductory course to Python programming.",
            instructor="southdog",
            start_date=date(2024, 7, 10),
            end_date=None,
            topics=["Python Basics", "Data Structures", "Functions", "Modules"],
            price=5000
        )

if __name__ == "__main__":
    pytest.main()
