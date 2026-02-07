from waitress import serve
from app import app

print("Starting Barcode Flask API with Waitress...")

serve(
    app,
    host="127.0.0.1",
    port=5001,
    threads=8   # adjust later if needed
)
