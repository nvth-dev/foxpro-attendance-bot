Các thư viện cần thiết trước khi chạy bot server
```
psutil==6.1.1
python-telegram-bot==13.13
Requests==2.32.3
```

Sửa tệp `maindev/your_information.py`

Những thông tin cần phải sửa 

![edit-information](img/image.png)

Để dùng song song giữa telegram bot và app checkin, thay đổi thông tin jwt trong `maindev/db/update_jwt_manual.py`

Chỉnh sửa biến access_token

![alt text](img/image2.png)

Sau đó sử dụng command dưới đây để cập nhật jwt manual

> python3 maindev/db/update_jwt_manual.py

Lưu ý: Sử dụng burpsuite bắt request app lấy jwt trên

để chạy ẩn server bot telegram, sử dụng command

> python3 maindev/run.py 


Các command tương tác với bot telegram sau khi chạy thành công script

```
/c : checkin
/o : checkout
/p : Lấy thông tin người dùng (tên, seniority)
/a month date : Gọi danh sách lấy lịch trong tháng
```

