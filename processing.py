import os.path
import cv2
from PySide6 import QtWidgets

class ImageProcessor:
    def __init__(self):
        self.locations = []

    def is_folder_valid(self, folder):
        return os.path.exists(folder)

    def get_valid_image_files(self, folder):
        file_list = os.listdir(folder)
        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".gif",))
        ]
        return fnames

    def get_absolute_file_path(self, folder, filename):
        return os.path.join(folder, filename)

    def save_coordinates(self):
        with open("coordinates.txt", "w") as f:
            for i, coord in enumerate(self.locations):
                f.write(f"{i + 1} = X:{coord[0]}, Y:{coord[1]}\n")

    def process_image(self, filename):
        img = cv2.imread(filename)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, threshold = cv2.threshold(gray, 40, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(
            threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for i, contour in enumerate(contours):
            if i == 0:
                continue

            cv2.drawContours(img, [contour], 0, (0, 0, 255), 1)

            M = cv2.moments(contour)
            if M['m00'] != 0.0:
                x = int(M['m10'] / M['m00'])
                y = int(M['m01'] / M['m00'])
                self.locations.append((x, y))

                text = f"{i}"
                cv2.putText(img, text, (x, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)

        cv2.imwrite("processedimage.png", img)
        self.save_coordinates()
        QtWidgets.QMessageBox.information(None, "Success", "New image created")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
