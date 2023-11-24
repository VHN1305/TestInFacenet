# TestInFacenet

Project Pizza Error Classification

Mô tả đề tài: Đề tài này được tôi thực hiện tại trong quá trình thực công ty Facenet, đề tài được mô tả như sau:
- Với các nhãn hàng Pizza, việc kiểm thử bánh khi mới ra khỏi lò là rất rất cần thiết, do đó việc xây dựng mô hình phát hiện lỗi sai trong mỗi ảnh pizza mới ra khỏi lò sẽ đảm bảo được chất lượng bánh khi đến tay khách hàng
- Dữ liệu được cung cấp là ảnh chụp những chiếc pizza khi mới ra khỏi lò, nhãn là các loại lỗi của chiếc pizza đó, ví dụ như: Cháy, Viền bánh nhỏ,... Có tất cả 23 lỗi, tuy vậy có 1 vài lỗi có số mẫu rất nhỏ nên tôi bỏ qua những lỗi như vậy. Do đó còn tất cả 20 lỗi, và đây là bài toàn phân loại ảnh với đầu ra là multylabel
- Tôi đã huấn luyện mô hình trên kaggle bởi kaggle cung cấp GPU khá khỏe, thuận tiện cho việc học từ tập ảnh. Cách tôi huấn luyện mô hình có trong file model-train.ipynb. Tôi sử dụng kiến trúc mạng InceptionV3 để học, bởi bài toán cũng có giới hạn về kích thước của mô hình
- Tôi có xây dựng 1 web đơn giản để demo cho mô hình, dưới đây là ảnh minh họa
  ![image](https://github.com/VHN1305/TestInFacenet/assets/86543998/d91557d4-1f26-4fce-925c-d8e9d5a19b2c)
