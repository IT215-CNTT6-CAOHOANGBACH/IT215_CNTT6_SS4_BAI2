# Phân tích lỗi:
# câu 1:Endpoint hiện tại có Path Parameter không?
# Có. Endpoint hiện tại có Path Parameter là:
# @app.get("/orders/status/{status}")



# câu 2:Path Parameter trong bài này là gì? 
# Là status

# câu 3: Khi gọi /orders/status/pending, biến status nhận giá trị gì?
# biến status sẽ nhận giá trị: pending


# câu 4:Vì sao API hiện tại trả về sai dữ liệu?
# vì API trả về toàn bộ danh sách orders mà không lọc theo giá trị status được truyền từ URL



# câu 5: Dòng code nào đang khiến API bỏ qua giá trị status?
# return orders, vì dòng này trả về tất cả đơn hàng.




from fastapi import FastAPI
app = FastAPI()
orders = [
    {"id": 1, "customer_name": "Nguyễn Văn An", "total": 250000, "status": "pending"},
    {"id": 2, "customer_name": "Trần Thị Bình", "total": 500000, "status": "paid"},
    {"id": 3, "customer_name": "Lê Văn Cường", "total": 150000, "status": "cancelled"},
    {"id": 4, "customer_name": "Phạm Thị Dung", "total": 320000, "status": "pending"}
]
@app.get("/orders/status/{status}")
def get_orders_by_status(status: str):
    valid_status = ["pending", "paid", "cancelled"]

    if status not in valid_status:
        return {
            "message": "Trạng thái đơn hàng không hợp lệ"
        }
    
    result = []
    
    for order in orders:
        if order.get("status") == status:
            result.append(order)

    return result