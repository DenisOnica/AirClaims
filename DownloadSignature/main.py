import base64

# Replace this with the base64-encoded signature retrieved from MongoDB
base64_signature = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIsAAACGCAYAAADth3khAAAN…"

# Remove data URI prefix if present
if base64_signature.startswith('data:image/png;base64,'):
    base64_data = base64_signature.split(',')[1]  # Remove prefix
else:
    base64_data = base64_signature

# Decode base64 data
try:
    # Ensure that the base64_data is converted to bytes before decoding
    base64_bytes = base64_data.encode('utf-8')
    signature_bytes = base64.b64decode(base64_bytes)
    print("Base64 decoding successful.")

    # Optional: Save decoded bytes as a PNG file for verification
    with open('decoded_signature.png', 'wb') as f:
        f.write(signature_bytes)

    print("Saved decoded signature as 'decoded_signature.png'. Verify manually.")

except Exception as e:
    print(f"Error decoding base64 data: {e}")
