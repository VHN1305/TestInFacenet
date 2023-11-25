import os
import requests
import pandas as pd

if __name__ == '__main__':
    csv_file_path = 'data\pizza_error_list_with_label.csv'

    # Đọc dữ liệu từ CSV vào DataFrame
    data = pd.read_csv(csv_file_path)

    # Tạo thư mục để lưu trữ ảnh nếu chưa tồn tại
    output_folder = 'downloaded_images'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Lặp qua từng dòng trong DataFrame và tải ảnh
    for index, row in data.iterrows():
        image_url = row['image_url']
        image_id = row['_id'] + '.jpg'  # Đặt tên cho ảnh

        # Kiểm tra xem ảnh đã tồn tại trong thư mục hay chưa
        image_path = os.path.join(output_folder, image_id)
        if os.path.exists(image_path):
            print(f"Ảnh {image_id} đã tồn tại, không cần tải lại.")
            continue

        # Thực hiện tải ảnh từ URL
        response = requests.get(image_url)

        # Kiểm tra xem request có thành công hay không (status code 200)
        if response.status_code == 200:
            # Mở file và lưu dữ liệu tải về
            with open(image_path, "wb") as file:
                file.write(response.content)
            print(f"Ảnh {image_id} đã được tải và lưu vào {image_path}")
        else:
            print(f"Lỗi khi tải ảnh {image_id}, status code: {response.status_code}")

    print("Quá trình tải ảnh hoàn tất.")