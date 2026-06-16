# Upload image first
IMAGE=$(postiz upload photo.jpg)
IMAGE_URL=$(echo "$IMAGE" | jq -r '.path')
