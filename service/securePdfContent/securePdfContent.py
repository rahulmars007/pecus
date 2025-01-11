from pdf2image import convert_from_path
from PIL import Image
import os


def securePdf(path_to_upload):
    try:
        pdf_path = os.path.join(path_to_upload, 'sample.pdf')
        # Convert PDF to images
        images = convert_from_path(pdf_path, dpi=120, poppler_path=r'.\poppler\bin')

        # Save each image to the output directory
        image_paths = []
        for idx, image in enumerate(images):
            image_path = os.path.join(path_to_upload, f"page_{idx + 1}.jpg")
            image.save(image_path, "JPEG")
            image_paths.append(image_path)

        # Convert images back into a single PDF
        pdf_output_path = os.path.join(path_to_upload, "secure.pdf")
        image_objs = [Image.open(img).convert("RGB") for img in image_paths]
        image_objs[0].save(
            pdf_output_path,
            save_all=True,
            append_images=image_objs[1:]
        )
        #return pdf_output_path
    except Exception as e:
        raise RuntimeError(f"Error processing the PDF: {e}")