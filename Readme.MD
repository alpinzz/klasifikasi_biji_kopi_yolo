# Training Result

Hasil training akan tersimpan di:

```txt
runs/detect/detect_coffe/
```

File penting:

| File                 | Fungsi          |
| -------------------- | --------------- |
| best.pt              | Model terbaik   |
| last.pt              | Model terakhir  |
| results.png          | Grafik training |
| confusion_matrix.png | Matrix evaluasi |

---

# Prediction / Detection

## Struktur Folder

```txt
project/
│
├── input_images/
└── test.py
```

Masukkan gambar ke folder `input_images`.

# Output Result

Hasil deteksi akan tersimpan di:

```txt
runs/detect/output/predict/
```

# Requirements

- Python 3.10+
- Ultralytics
