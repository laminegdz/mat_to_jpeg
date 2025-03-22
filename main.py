import os
import h5py
import numpy as np
from PIL import Image


input_folder = 'fichier_matlab'
output_folder = 'image_jpeg'


os.makedirs(output_folder, exist_ok=True)


def convert_mat_mri_to_jpeg(mat_file_path, output_image_path):
    with h5py.File(mat_file_path, 'r') as mat_file:
        image_data = mat_file['cjdata/image'][:]
    #regler le contraste
    min_val = image_data.min()
    max_val = image_data.max()
    normalized_image = ((image_data - min_val) / (max_val - min_val)) * 255
    normalized_image_uint8 = normalized_image.astype(np.uint8)
    image = Image.fromarray(normalized_image_uint8)
    image.save(output_image_path)
    print(f" Converti: {mat_file_path} vers {output_image_path}")



#boucler sur tout le dossier fichier_matlab
def convert_all_mat_files():
    for filename in os.listdir(input_folder):
        if filename.endswith('.mat'):
            mat_path = os.path.join(input_folder, filename)
            jpeg_name = os.path.splitext(filename)[0] + '.jpg'
            jpeg_path = os.path.join(output_folder, jpeg_name)
            
            try:
                convert_mat_mri_to_jpeg(mat_path, jpeg_path)
                os.remove(mat_path)
                print(f"supprimé: {mat_path}")
            except Exception as e:
                print(f"erreur {filename}: {e}")

if __name__ == "__main__":
    convert_all_mat_files()
