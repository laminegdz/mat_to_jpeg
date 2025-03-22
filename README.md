
---

## 💡 Why I Built This

I was working with medical imaging datasets, specifically **brain tumor scans stored in MATLAB format**, and I needed a fast way to:
- Visualize them without MATLAB
- Convert them to standard image format
- Prepare them for ML pipelines

So I built this script to **batch convert** `.mat` MRI data into clean, normalized `.jpg` files — with tumor visibility preserved.

---

## 🔍 What It Does

- Scans `fichier_matlab/` for all `.mat` files
- Extracts the `cjdata/image` field (standard in brain MRI sets)
- Normalizes intensity using full dynamic range (no contrast loss)
- Converts to `.jpg` and saves in `image_jpeg/`
- Deletes the original `.mat` file after successful conversion

---

## 📊 Requirements

Install the required packages with:

```bash
pip install h5py numpy Pillow
