import camera_model
import camera_view
from threading import Thread

class Controller:
    def __init__(self):
        self.root = camera_view.tk.Tk()
        self.root.geometry("800x480")
        self.app = camera_view.Application(master=self.root)
        self.nominal_images = []
        self.discrepancy_images = []
        self.video_feed_running = False

        # Connect buttons to controller methods
        self.app.nominal_button["command"] = self.capture_nominal
        self.app.discrepancy_button["command"] = self.capture_discrepancy
        self.app.reset_button["command"] = self.reset
        self.app.video_feed_button["command"] = self.toggle_video_feed

    def capture_nominal(self):
        image_name = "nominal_image.jpg"
        camera_model.capture_photo(image_name)
        self.nominal_images.append(image_name)
        self.update_labels()

    def capture_discrepancy(self):
        image_name = "discrepancy_image.jpg"
        camera_model.capture_photo(image_name)
        self.discrepancy_images.append(image_name)
        self.update_labels()

    def reset(self):
        self.nominal_images = []
        self.discrepancy_images = []
        self.update_labels()

    def toggle_video_feed(self):
        if self.app.video_feed_button["text"] == "Start Video Feed":
            self.app.video_feed_button["text"] = "Stop Video Feed"
            self.video_feed_running = True
            self.update_video_feed()
        else:
            self.app.video_feed_button["text"] = "Start Video Feed"
            self.video_feed_running = False

    def update_video_feed(self):
        if not self.video_feed_running:
            return

        frame = camera_model.get_camera_frame()
        self.video_feed_image = camera_view.ImageTk.PhotoImage(frame)
        self.app.video_feed_label["image"] = self.video_feed_image

        # Update the video feed every 100 milliseconds
        self.root.after(100, self.update_video_feed)

    def update_labels(self):
        nominal_diff = camera_model.compare_images(self.nominal_images[-1], self.nominal_images[-2]) if len(self.nominal_images) > 1 else 0
        discrepancy_diff = camera_model.compare_images(self.discrepancy_images[-1], self.discrepancy_images[-2]) if len(self.discrepancy_images) > 1 else 0
        discrepancy_range = camera_model.compare_images(self.nominal_images[-1], self.discrepancy_images[-1]) if self.nominal_images and self.discrepancy_images else 0

        self.app.nominal_label["text"] = f"Nominal images: {len(self.nominal_images)}, difference: {nominal_diff}"
        self.app.discrepancy_label["text"] = f"Discrepancy images: {len(self.discrepancy_images)}, difference: {discrepancy_diff}, range: {discrepancy_range}"

    def run(self):
        self.app.mainloop()

if __name__ == "__main__":
    controller = Controller()
    controller.run()
