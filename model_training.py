# Copyright 2023 The MediaPipe Authors.
# Licensed under the Apache License, Version 2.0 (the "License");
#
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
PYTHON_ISOLATE_WORKER_DEPENDENCIES = 1
PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION= "python"


import os
import tensorflow as tf
assert tf.__version__.startswith('2')

from mediapipe_model_maker import gesture_recognizer

import matplotlib.pyplot as plt

def main():
  
  dataset_path = "./hand_signal_data"

  print(dataset_path)
  labels = []
  for i in os.listdir(dataset_path):
    if os.path.isdir(os.path.join(dataset_path, i)):
      labels.append(i)
  print(labels)
  
  NUM_EXAMPLES = 5

  for label in labels:
    label_dir = os.path.join(dataset_path, label)
    example_filenames = os.listdir(label_dir)[:NUM_EXAMPLES]
    fig, axs = plt.subplots(1, NUM_EXAMPLES, figsize=(10,2))
    for i in range(NUM_EXAMPLES):
      axs[i].imshow(plt.imread(os.path.join(label_dir, example_filenames[i])))
      axs[i].get_xaxis().set_visible(False)
      axs[i].get_yaxis().set_visible(False)
    fig.suptitle(f'Showing {NUM_EXAMPLES} examples for {label}')

    #plt.show()
    
  data = gesture_recognizer.Dataset.from_folder(
      dirname=dataset_path,
      hparams=gesture_recognizer.HandDataPreprocessingParams()
  )
  train_data, rest_data = data.split(0.8)
  validation_data, test_data = rest_data.split(0.5)
  
  hparams = gesture_recognizer.HParams(export_dir="exported_model")
  options = gesture_recognizer.GestureRecognizerOptions(hparams=hparams)
  model = gesture_recognizer.GestureRecognizer.create(
      train_data=train_data,
      validation_data=validation_data,
      options=options
  )
  
  loss, acc = model.evaluate(test_data, batch_size=1)
  print(f"Test loss:{loss}, Test accuracy:{acc}")
  
  model.export_model()
  


if __name__ == '__main__':
    main()