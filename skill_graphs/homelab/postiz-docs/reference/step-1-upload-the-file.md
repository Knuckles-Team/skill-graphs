# Step 1: upload the file
curl -X POST "https://api.postiz.com/public/v1/upload" \
  -H "Authorization: your-api-key" \
  -F "file=@photo.jpg"
