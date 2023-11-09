import tensorflow as tf
from keras import models
import requests
import os

# load model

LABELS = [
    "Cháy_Baking-Burnt",
    "Khôngđốm_Baking-Doesnothaveleopard-spotting",
    "Màunhạt_Baking-Pale",
    "Lênmenthiếu_Fermentation-Lackfermentation",
    "Viềnkđều_Edge-Uneven",
    "Viềnnhỏ_Edge-Toosmall",
    "Viềnto_Edge-Toobig",
    "Viềnthấp_Edge-Toolow",
    "Quátheoviền_Topping-Toostrongshapingtheedge",
    "Topping-Khôngđúng_incorrectportioning",
    "KhôngcânTopping-Notevenhalfandhalf",
    "Sốttrênmép_Topping-Saucecoveringontheedge",
    "Trộnlẫn_Topping-Bended",
    "Quátậptrung_Topping-Toppingtoocentered",
    "Topping-Khôngđều_Noteven",
    "Thiếubóng_toofewballs",
    "Nởviềnkhôngđủ_edgepizzaisnotenoughswollen",
    "Bánhkhôngtròn_Distortedshape",
    "Bánhbé_Size-Toosmall",
    "Phômaicao_Topping-Cheesetoohigh"
]
def load_model():
    best_model = models.load_model('model/best_model/best_model.h5')
    return best_model

def download_image(url, folder_path="uploads"):
    try:
        # Kiểm tra xem thư mục có tồn tại hay không, nếu không tồn tại thì tạo mới
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Tạo đường dẫn lưu ảnh
        image_path = os.path.join(folder_path, os.path.basename(url))

        # Tải ảnh từ URL
        response = requests.get(url)

        # Kiểm tra xem request có thành công hay không (status code 200)
        if response.status_code == 200:
            # Mở file và lưu dữ liệu tải về
            with open(image_path, "wb") as file:
                file.write(response.content)
            print(f"Ảnh đã được tải và lưu vào {image_path}")
        else:
            print(f"Lỗi khi tải ảnh, status code: {response.status_code}")

        return image_path

    except Exception as e:
        print(f"Lỗi: {e}")


def decode_predictions(predict):
    result = []
    for i in range(len(predict)):
        result.append([])
        for j in range(len(predict[i])):
            temp = ""
            if predict[i][j] > 0.5:
                temp = LABELS[j] + " " + str(round(predict[i][j] * 100, 2)) + "%" + " "
                result[i].append(temp)
    return result


def predict_image(path):
    # Read image
    image = tf.keras.preprocessing.image.load_img(path, target_size=(224, 224))
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = image.reshape((1,) + image.shape)
    image /= 255.0
    model = load_model()

    result = model.predict(image, verbose=1)

    name_results = decode_predictions(result)
    if (name_results == [[]]):
        return [["Ảnh không có lỗi"]]

    new_result = name_results[0]

    return new_result


if __name__ == "__main__":
    predict = predict_image("uploads/20230531_103633_LTT_LTT-01_29f750aa.jpg")
    print(predict)


# i want to load model