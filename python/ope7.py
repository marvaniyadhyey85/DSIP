import cv2 
import numpy as np 
import os 
def ensure_uint8(image): 
    """Detects 16-bit PNGs and safely converts them to 8-bit 0-255.""" 
    if image is None: 
        return None 
    print(f"  -> Input dtype: {image.dtype}, Min: {np.min(image)}, Max: {np.max(image)}") 
     
    if image.dtype == 'uint16': 
        print("  ⚠️ Detected 16-bit PNG. Scaling down to 8-bit...") 
        image = (image / 256.0).astype('uint8') 
    elif image.dtype != 'uint8': 
        image = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX).astype('uint8') 
     
    print(f"  -> Converted to dtype: {image.dtype}, Min: {np.min(image)}, Max: {np.max(image)}") 
    return image 
 
# ========================================== 
# 2. ENHANCEMENT FUNCTIONS 
# ========================================== 
 
def gamma_correction(image, gamma=1.0): 
    inv_gamma = 1.0 / gamma 
    table = np.array([((i / 255.0) ** inv_gamma) * 255 for i in np.arange(0, 256)]).astype("uint8") 
    return cv2.LUT(image, table) 
 
def contrast_stretching(image, lower_percent=2, upper_percent=98): 
    min_val, max_val = np.percentile(image, (lower_percent, upper_percent)) 
    if max_val - min_val == 0: 
        return image 
    stretched = (image - min_val) * (255.0 / (max_val - min_val)) 
    return np.clip(stretched, 0, 255).astype(np.uint8) 
 
def clahe_enhancement(image, clip_limit=2.0, grid_size=(8, 8)): 
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=grid_size) 
    return clahe.apply(image) 
 
# Update to your exact .png file names 
input_files = { 
    'img1': 'image1.png',  # Washed-out Seeds 
    'img2': 'image2.png',  # Circular Pattern 
    'img3': 'image3.png',  # Dark Seeds 
    'img4': 'image4.png',  # Night Car 
       'img5': 'image5.png'   # CT Scan 
} 
print("--- Starting ROBUST Enhancement Pipeline ---\n") 
# --- IMAGE 1: Contrast Stretching --- 
if os.path.exists(input_files['img1']): 
    img1 = cv2.imread(input_files['img1'], cv2.IMREAD_GRAYSCALE) 
    img1 = ensure_uint8(img1) 
    img1_out = contrast_stretching(img1, lower_percent=2, upper_percent=98) 
    cv2.imwrite('image1_enhanced.png', img1_out) 
    print(f"✓ Enhanced {input_files['img1']} -> image1_enhanced.png\n") 
 
# --- IMAGE 2: Stretch FIRST, THEN CLAHE to avoid black-out --- 
if os.path.exists(input_files['img2']): 
    img2 = cv2.imread(input_files['img2'], cv2.IMREAD_GRAYSCALE) 
    img2 = ensure_uint8(img2) 
    # Stretch the extremely flat image first to give CLAHE data to work with 
    img2_stretched = contrast_stretching(img2, lower_percent=1, upper_percent=99) 
    # Then apply CLAHE to get the rings clearly 
    img2_out = clahe_enhancement(img2_stretched, clip_limit=2.0, grid_size=(8, 8)) 
    cv2.imwrite('image2_enhanced.png', img2_out) 
    print(f"✓ Enhanced {input_files['img2']} -> image2_enhanced.png\n") 
 
# --- IMAGE 3: Stretch FIRST, THEN Gamma 0.35 --- 
if os.path.exists(input_files['img3']): 
    img3 = cv2.imread(input_files['img3'], cv2.IMREAD_GRAYSCALE) 
    img3 = ensure_uint8(img3) 
    # Lift the ultra-dark pixels first, otherwise Gamma(0) = 0 
    img3_stretched = contrast_stretching(img3, lower_percent=0, upper_percent=100) 
    # Now apply Gamma to naturally brighten the visible seeds 
    img3_out = gamma_correction(img3_stretched, gamma=0.35) 
    cv2.imwrite('image3_enhanced.png', img3_out) 
    print(f"✓ Enhanced {input_files['img3']} -> image3_enhanced.png\n") 
 
# --- IMAGE 4: NIGHT CAR - FIXED USING CLAHE LOCAL BRIGHTENING --- 
if os.path.exists(input_files['img4']): 
    img4 = cv2.imread(input_files['img4'], cv2.IMREAD_GRAYSCALE) 
    img4 = ensure_uint8(img4) 
    
    # Step 1: Global Stretch (Clip top 1% to prevent the bright lamp from ruining the scale) 
    img4_stretched = contrast_stretching(img4, lower_percent=0, upper_percent=99) 
     
    # Step 2: CLAHE (The FIX). It looks at 8x8 blocks of the car.  
    # Since the car is black, CLAHE forces those blocks to stretch into visible grays. 
    img4_clahe = clahe_enhancement(img4_stretched, clip_limit=4.0, grid_size=(8, 8))
      # Step 3: Mild Gamma to get a natural aesthetic tone 
    img4_out = gamma_correction(img4_clahe, gamma=0.6) 
     
    # Step 4: Unsharp Mask for crisp edges 
    blurred = cv2.GaussianBlur(img4_out, (0, 0), 1) 
    img4_out = cv2.addWeighted(img4_out, 1.0 + 1.0, blurred, -1.0, 0) 
    
    cv2.imwrite('image4_enhanced.png', img4_out) 
    print(f"✓ Enhanced {input_files['img4']} -> image4_enhanced.png (CLAHE local fix)\n") 
# --- IMAGE 5: CT Scan (CLAHE) --- 
if os.path.exists(input_files['img5']): 
    img5 = cv2.imread(input_files['img5'], cv2.IMREAD_GRAYSCALE) 
    img5 = ensure_uint8(img5) 
    # Lift slightly, then CLAHE to reveal organs clearly 
    img5_stretched = contrast_stretching(img5, lower_percent=1, upper_percent=99) 
    img5_out = clahe_enhancement(img5_stretched, clip_limit=2.0, grid_size=(8, 8)) 
    cv2.imwrite('image5_enhanced.png', img5_out) 
    print(f"✓ Enhanced {input_files['img5']} -> image5_enhanced.png\n") 
print("--- All images processed successfully! Check your folder. ---")