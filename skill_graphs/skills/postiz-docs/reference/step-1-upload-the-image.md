# Step 1: Upload the image
curl -X POST "https://api.postiz.com/public/v1/upload" \
  -H "Authorization: your-api-key" \
  -F "file=@photo.jpg"
