import pickle
import numpy as np
import sys

# Load the NPZ file
npz_path = sys.argv[1]  # Replace with your actual file path
amass_data_path = "dance_stand_poses.npz" 

#data = np.load(npz_path, allow_pickle=True)
amass_data = np.load(amass_data_path, allow_pickle=True)
data = np.load(npz_path, allow_pickle=True)

gesture_pelvis_rotation = data["poses"][0, :3]  # First frame
amass_pelvis_rotation = amass_data["poses"][0, :3]  # First frame

# Apply AMASS pelvis rotation to gesture data
corrected_gesture_data = {key: data[key] for key in data.files}  # Copy data
corrected_gesture_data["poses"][:, :3] = amass_pelvis_rotation  # 


corrected_gesture_data['mocap_framerate'] = corrected_gesture_data['mocap_frame_rate']
# Save as a pickle file
pkl_path = npz_path.replace("npz","pkl")
with open(pkl_path, "wb") as f:
    pickle.dump(corrected_gesture_data, f)

print(f"Conversion complete: {pkl_path}")