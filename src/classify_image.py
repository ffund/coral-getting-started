import argparse
from edgetpu.classification.engine import ClassificationEngine
from edgetpu.utils import dataset_utils
from PIL import Image


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument(
      '--model', help='File path of Tflite model.', required=True)
  parser.add_argument('--label', help='File path of label file.', required=True)
  parser.add_argument(
      '--image', help='File path of the image to be recognized.', required=True)
  args = parser.parse_args()

  # Prepare labels.
  labels = dataset_utils.read_label_file(args.label)
  # Initialize engine.
  engine = ClassificationEngine(args.model)
  # Run inference.
  img = Image.open(args.image)
  for result in engine.classify_with_image(img, top_k=3):
    print('---------------------------')
    print(labels[result[0]])
    print('Score : ', result[1])


if __name__ == '__main__':
  main()