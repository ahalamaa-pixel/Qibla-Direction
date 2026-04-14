import fitz
import os

pdf_path = "Celestial_Qibla_Guide.pdf"
doc = fitz.open(pdf_path)

output_dir = "pdf_images"
os.makedirs(output_dir, exist_ok=True)

print(f"Total pages: {len(doc)}")
for page_num in range(len(doc)):
    page = doc.load_page(page_num)
    text = page.get_text()
    print(f"--- Page {page_num + 1} Text ---")
    print(text)
    
    images = page.get_images(full=True)
    if images:
        print(f"--- Page {page_num + 1} Images ---")
        for img_index, img in enumerate(images):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            ext = base_image["ext"]
            img_filename = f"{output_dir}/page_{page_num+1}_img_{img_index+1}.{ext}"
            with open(img_filename, "wb") as f:
                f.write(image_bytes)
            print(f"Saved image: {img_filename}")

doc.close()
