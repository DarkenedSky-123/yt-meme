import cv2

def detect_video_cuts(video_path, threshold=1000):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video file.")
        return
    
    prev_frame = None
    prev_blurred = None
    cut_indices = []
    frame_count = 0
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        frame_count += 1
        
        # Convert to grayscale for easier comparison
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        if prev_frame is not None:
            # Blur the frames
            blurred_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)
            prev_blurred = cv2.GaussianBlur(prev_frame, (5, 5), 0)
            
            # Calculate absolute difference between blurred frames
            frame_diff = cv2.absdiff(prev_blurred, blurred_frame)
            
            # Calculate how "noisy" the frame difference is
            noise_level = frame_diff.std()
            
            if noise_level > threshold:
                # Round the cut index to two decimal places and append to cut_indices
                cut_indices.append(round(frame_count/30, 1))  # Assuming frame rate is 30 frames per second
        
        prev_frame = gray_frame
    
    cap.release()
    return cut_indices

# Example usage:
video_path = "video.mp4"
cuts = detect_video_cuts(video_path, threshold=52)  # Adjust threshold value as needed

# Print the detected cuts with values rounded to two decimal places
print("Detected cuts at frames:", cuts)

with open("cuts.txt",'a')as f:
    f.write
    l=len(cuts)
    for i in range (0,l,1):
        f.write((str)(cuts[+i]))