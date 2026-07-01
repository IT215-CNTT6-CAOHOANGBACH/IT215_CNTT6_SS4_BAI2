"""  
STT | Dữ liệu gửi lên                       | Kết quả hiện tại | Kết quả đúng mong muốn                     | Lỗi phát hiện
1	| student_id = "SV001", course_id = 1	| Vẫn đăng ký được | Báo lỗi học viên đã đăng ký khóa học này	| Không kiểm tra đăng ký trùng
2	| student_id = "SV002", course_id = 1	| Vẫn đăng ký được | Báo lỗi học viên đã đăng ký khóa học này	| Cho phép trùng bản ghi (student + course)
"""


from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

enrollments = [
    {"id": 1, "student_id": "SV001", "course_id": 1},
    {"id": 2, "student_id": "SV002", "course_id": 1}
]

class EnrollmentCreate(BaseModel):
    student_id: str
    course_id: int

# Thêm status_code=201 cho trường hợp tạo thành công
@app.post("/enrollments", status_code=status.HTTP_201_CREATED)
def create_enrollment(enrollment: EnrollmentCreate):
    # Kiểm tra xem học viên đã đăng ký khóa học này chưa
    for item in enrollments:
        if item["student_id"] == enrollment.student_id and item["course_id"] == enrollment.course_id:
            # Nếu trùng, trả về lỗi HTTPException
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Học viên đã đăng ký khóa học này trước đó."
            )
    
    # Nếu không trùng, tạo đăng ký mới
    new_enrollment = {
        "id": len(enrollments) + 1,
        "student_id": enrollment.student_id,
        "course_id": enrollment.course_id
    }
    enrollments.append(new_enrollment)
    
    return {
        "message": "Enroll successfully",
        "data": new_enrollment
    }