from keras.models import load_model
from tensorflow import keras
import tensorflow as tf
 
# Root path
root_path_drive = 'gdrive/My Drive/deep learning project/'
root_path = 'D:\\Master\\Galaxy Zoo dataset\\dataset for classification folder\\'

# File path for model
model_file = 'save_at_50.h5'
model_path = "".join([root_path, model_file])

# File path for training image directory
img_file_train = 'dataset 2000'

# Image file path for model prediction
img_file_early = '156975.jpg'
img_file_late = '295305.jpg'
img_path_early = "".join([root_path_drive,'early\\',img_file_early])
img_path_late = "".join([root_path_drive,'late\\',img_file_late])

# Load image directory
image_dir = "".join([root_path, img_file_train])

# Create dataset
image_size = (300, 300)
batch_size = 32

train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    image_dir,
    validation_split=0.3,
    subset="training",
    seed=1337,
    image_size=image_size,
    batch_size=batch_size,
)
val_ds = tf.keras.preprocessing.image_dataset_from_directory(
    image_dir,
    validation_split=0.3,
    subset="validation",
    seed=1337,
    image_size=image_size,
    batch_size=batch_size,
)

# load model
model = load_model(model_path)

# Evaluate model on evaluation image dataset
model.evaluate(val_ds)

# Create img array for prediction
img = keras.preprocessing.image.load_img(
    img_path_early, target_size=image_size
)
img_array = keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)  # Create batch axis

# Model prediction: 1 - Early type | 0 - Late type
predictions = model.predict(img_array)
score = predictions[0]
print(
    "This image is %.2f percent (Early type galaxy) and %.2f percent (Late type galaxy)."
    % (100 * (1 - score), 100 * score)
)