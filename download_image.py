import os
import requests
import pandas as pd

def download_error_image(csv_file_path, output_folder, num_images_with_errors_per_error=200):
    # Đọc dữ liệu từ file CSV
    df = pd.read_csv(csv_file_path)

    # Lấy danh sách các lỗi
    unique_errors = df.columns[2:].tolist()

    # Tạo thư mục cho ảnh có lỗi
    error_folder = os.path.join(output_folder, "error")
    if not os.path.exists(error_folder):
        os.makedirs(error_folder)

    # Tải và lưu ảnh vào thư mục con
    for error in unique_errors:
        # Lấy các ảnh bị lỗi cho từng loại lỗi
        images_with_errors = df[df[error] == 1]
        selected_images = images_with_errors['image_url'][:num_images_with_errors_per_error].tolist()

        # Tạo thư mục con cho loại lỗi
        error_subfolder = os.path.join(error_folder, error.replace(" ", "_"))
        if not os.path.exists(error_subfolder):
            os.makedirs(error_subfolder)

        # Tải và lưu ảnh
        for idx, image_url in enumerate(selected_images):
            response = requests.get(image_url)
            if response.status_code == 200:
                image_id = images_with_errors.iloc[idx]['_id']
                image_file_name = f"{image_id}.jpg"
                image_path = os.path.join(error_subfolder, image_file_name)
                with open(image_path, 'wb') as image_file:
                    image_file.write(response.content)
                    print(f"Tải và lưu {image_file_name} thành công cho ảnh có lỗi loại {error}")
            else:
                print(f"Lỗi khi tải ảnh từ URL {image_url}")

    print(f"Hoàn thành quá trình tải ảnh có lỗi.")


def download_non_error_image(csv_file_path, output_folder, num_images_without_errors=200):
    # Đọc dữ liệu từ file CSV
    df = pd.read_csv(csv_file_path)
    
    # Số lượng ảnh cần tải mà không bị lỗi
    images_without_errors = df[df.iloc[:, 2:].sum(axis=1) == 0]
    
    # Lấy tối đa num_images_without_errors ảnh đầu tiên mà không bị lỗi
    selected_images = images_without_errors['image_url'][:num_images_without_errors].tolist()

    # Tạo thư mục cho ảnh không có lỗi
    no_error_folder = os.path.join(output_folder, "no_error")
    if not os.path.exists(no_error_folder):
        os.makedirs(no_error_folder)
    
    # Tải và lưu ảnh vào thư mục con
    for idx, image_url in enumerate(selected_images):
        response = requests.get(image_url)
        if response.status_code == 200:
            image_id = images_without_errors.iloc[idx]['_id']
            image_file_name = f"{image_id}.jpg"
            image_path = os.path.join(no_error_folder, image_file_name)
            with open(image_path, 'wb') as image_file:
                image_file.write(response.content)
                print(f"Tải và lưu {image_file_name} thành công cho ảnh không có lỗi")
        else:
            print(f"Lỗi khi tải ảnh từ URL {image_url}")

    print(f"Hoàn thành quá trình tải ảnh mà không có lỗi.")

download_non_error_image('pizzacam\pizza_error_list_with_label.csv', 'image_input')
download_error_image('pizzacam\pizza_error_list_with_label.csv', 'image_input')

