from pdf2image import convert_from_path
from zipfile import ZipFile
import os


# def get_all_file_paths(directory):
#     file_paths = []
#     for root, directories, files in os.walk(directory):
#         for filename in files:
#             # join the two strings in order to form the full filepath.
#             filepath = os.path.join(root, filename)
#             file_paths.append(filepath)
#     return file_paths

# def pdf_to_image(path_to_upload): # required poppler for this operation
#         images = convert_from_path(path_to_upload+ '/sample.pdf',500,poppler_path=r'.\poppler\bin')
#         zipObj = ZipFile(path_to_upload + '/sample.zip', 'w')
#         new_path_to_upload = os.path.join(path_to_upload, "sample")
#         os.makedirs(new_path_to_upload)
#         for image in range(len(images)):
#             images[image].save(new_path_to_upload+'/page'+ str(image) +'.jpg', 'JPEG')
#             t=new_path_to_upload+'/page'+ str(image) +'.jpg'
#             zipObj.write(t)
#         zipObj.close()


def pdf_to_image(path_to_upload):  # required poppler for this operation
    try:
        # Convert PDF to images
        pdf_path = os.path.join(path_to_upload, 'sample.pdf')
        images = convert_from_path(pdf_path, dpi=120, poppler_path=r'.\poppler\bin')

        # Create directories for images and ZIP
        image_folder = os.path.join(path_to_upload, "sample")
        os.makedirs(image_folder, exist_ok=True)
        zip_path = os.path.join(path_to_upload, 'sample.zip')

        # Initialize ZIP file
        with ZipFile(zip_path, 'w') as zipObj:
            for idx, image in enumerate(images):
                # Save image as JPEG
                image_path = os.path.join(image_folder, f'page{idx}.jpg')
                image.save(image_path, 'JPEG')

                # Add image to ZIP file
                zipObj.write(image_path, arcname=f'page{idx}.jpg')
    except Exception as e:
        raise RuntimeError(f"Error during PDF to image conversion: {e}")