# Upload the video
VIDEO=$(postiz upload video.mp4)
VIDEO_URL=$(echo "$VIDEO" | jq -r '.path')
