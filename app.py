# # import sys
# # # Prevent Ultralytics from trying to import SAM and RTDETR
# # sys.modules["ultralytics.models.sam"] = None
# # sys.modules["ultralytics.models.rtdetr"] = None

# # from ultralytics import YOLO


# import streamlit as st
# import os
# import shutil
# import zipfile
# from ultralytics import YOLO
# from pathlib import Path
# import cv2
# from PIL import Image

# st.write("✅ OpenCV version:", cv2.__version__)


# # Load your trained YOLO model
# model = YOLO("best.pt")  # change to your best.pt

# # Temporary directories
# UPLOAD_DIR = "uploads"
# OUTPUT_DIR = "output"
# os.makedirs(UPLOAD_DIR, exist_ok=True)
# os.makedirs(OUTPUT_DIR, exist_ok=True)

# st.title("📦 Auto Image Annotation with YOLO")
# st.write("Upload a ZIP file of images or drag & drop images. Get back a YOLO dataset (images + labels).")

# uploaded_files = st.file_uploader("Upload images or a ZIP", accept_multiple_files=True, type=["jpg","jpeg","png","zip"])

# if uploaded_files:
#     # Clean old files
#     shutil.rmtree(UPLOAD_DIR, ignore_errors=True)
#     shutil.rmtree(OUTPUT_DIR, ignore_errors=True)
#     os.makedirs(UPLOAD_DIR, exist_ok=True)
#     os.makedirs(OUTPUT_DIR, exist_ok=True)

#     extracted_dir = os.path.join(UPLOAD_DIR, "extracted")
#     os.makedirs(extracted_dir, exist_ok=True)

#     # Save and extract if needed
#     for file in uploaded_files:
#         file_path = os.path.join(UPLOAD_DIR, file.name)
#         with open(file_path, "wb") as f:
#             f.write(file.getbuffer())

#         if file.name.endswith(".zip"):
#             with zipfile.ZipFile(file_path, "r") as zip_ref:
#                 zip_ref.extractall(extracted_dir)

#     # Choose directory to run YOLO on
#     image_dir = extracted_dir if any(f.name.endswith(".zip") for f in uploaded_files) else UPLOAD_DIR

#     # Run YOLO predictions
#     st.info("Running YOLO model... please wait ⏳")
#     results = model.predict(source=image_dir, save=True, save_txt=True, project=OUTPUT_DIR, name="results")

#     st.subheader("🔍 Preview Labeled Images")
#     result_dir = Path(OUTPUT_DIR) / "results"

#     predict_dirs = list(result_dir.glob("predict*"))
#     if predict_dirs:
#         image_files = list(predict_dirs[0].glob("*.jpg"))
#     else:
#         image_files = list(result_dir.glob("*.jpg"))


#     for img_path in image_files[:5]:  # show first 5 previews
#         st.image(str(img_path), caption=f"Preview: {img_path.name}")

#     # Prepare dataset structure
#     images_out = Path(OUTPUT_DIR) / "images"
#     labels_out = Path(OUTPUT_DIR) / "labels"
#     os.makedirs(images_out, exist_ok=True)
#     os.makedirs(labels_out, exist_ok=True)

#     # Move images
#     for img_file in Path(image_dir).iterdir():
#         if img_file.suffix.lower() in [".jpg", ".jpeg", ".png"]:
#             shutil.copy(img_file, images_out / img_file.name)

#     # Move labels
#     results_labels = Path(OUTPUT_DIR) / "results" / "labels"
#     if results_labels.exists():
#         for label_file in results_labels.iterdir():
#             shutil.move(str(label_file), labels_out / label_file.name)

#     # Create zip
#     zip_filename = Path(OUTPUT_DIR) / "dataset.zip"
#     shutil.make_archive(str(zip_filename).replace(".zip",""), 'zip', OUTPUT_DIR)

#     st.success("✅ Dataset ready!")
#     st.download_button("📥 Download YOLO Dataset", open(zip_filename, "rb"), file_name="dataset.zip")



import streamlit as st
import cv2
import pkg_resources

st.write("✅ OpenCV version:", cv2.__version__)
st.write("📦 Installed packages:", [p.project_name for p in pkg_resources.working_set if "opencv" in p.project_name.lower()])
