# Visual Inspection and Discrepancy Detection System

This project is a Python application designed for visual inspection tasks. It uses a camera to capture images, compares them against nominal (reference) images, and can identify discrepancies. The system also features the capability to control external hardware via relay modules, allowing for integration into automated testing setups. It provides a graphical user interface (GUI) for ease of operation.

## Installation

### Prerequisites

*   Python 3.x
*   pip (Python package installer)

### Steps

1.  **Clone the repository (if applicable):**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install the required Python libraries:**
    ```bash
    pip install opencv-python Pillow imagehash customtkinter RPi.GPIO
    ```
    *   **Note on `RPi.GPIO`**: This library is for interacting with GPIO pins on a Raspberry Pi. If you are not using a Raspberry Pi or do not need to control relays, you might be able to skip this package or the parts of the code that use it may not function. The application primarily uses a standard USB webcam.

## Usage

1.  **Navigate to the project directory where `camera_controller.py` is located.**
    If you followed the installation steps, this would typically be inside the `venv` directory, though it's unusual to have source code directly in `venv`.
    ```bash
    cd venv 
    ```
    *(Developer Note: Consider moving application source files out of the `venv` directory to the project root or a dedicated `src` directory for better project structure.)*

2.  **Run the application:**
    ```bash
    python camera_controller.py
    ```

### Features

The application window has two main tabs: "Threshold Setter" and "Discrepancy Finder".

*   **Video Feed:**
    *   Click the **"Viewfinder"** button (previously "Start Video Feed") on the main screen to start or stop a live video feed from the camera. This helps in positioning the camera and objects.
    *   The video feed will appear in a designated area of the UI.

*   **Threshold Setter Tab:**
    *   **Capture Nominal Image:** Click the **"Nominal"** button to capture a reference image. This image will be used as the baseline for comparisons.
    *   **Capture Discrepancy Image:** Click the **"Discrepancy"** button to capture an image that potentially has differences from the nominal image.
    *   **Labels:** The interface displays the number of nominal and discrepancy images captured, and the calculated difference or range between them. This helps in determining an appropriate threshold for discrepancy detection.

*   **Discrepancy Finder Tab:**
    *   **Settings:**
        *   **Threshold Slider:** Adjust the slider to set the sensitivity for detecting discrepancies. A higher value means only larger differences will be flagged.
    *   **Run:**
        *   Click the **"RUN"** button to start the automated discrepancy detection sequence.
    *   **Sequence:**
        *   This section allows you to define a series of actions to be performed during a test run.
        *   For each step in the sequence (up to 15 steps), you can select an action from the dropdown:
            *   **Delay:** Pause for a specified duration (you'll need to input the delay time in the entry box below the dropdown).
            *   **Image:** Capture an image and compare it against the nominal image using the set threshold.
            *   **Switch On:** Activate a specific relay (likely needs configuration in the code for which relay).
            *   **Switch Off:** Deactivate a specific relay.
        *   Use the entry field below each combobox to specify parameters for the action (e.g., delay duration, relay index).

*   **Reset Button:**
    *   Located on the main screen, click this button to clear all captured nominal and discrepancy images and reset the counters.

*   **Exit Button:**
    *   Click this to close the application.

## Configuration

### Camera

*   The application is configured to use a USB webcam by default, accessed via `cv2.VideoCapture(0)` in `venv/camera_model.py`.
*   If you need to use a different camera index, you may need to modify this line in `venv/camera_model.py`.
*   While the project includes `core.py` which uses `PiCamera`, the main application (`camera_controller.py`) currently uses `camera_model.py`, which points to the USB webcam.

### Relay Modules

*   Relay control is handled by functions in `venv/camera_model.py` (and also present in `venv/core.py`).
*   The GPIO pins for the relays are defined in the `RELAY_PINS` list within `venv/camera_model.py`:
    ```python
    RELAY_PINS = [11, 13, 15, 16, 18, 22, 29, 31]  # Board pin numbers
    ```
*   If you are using different GPIO pins for your relay module, you **must** update this list accordingly. Ensure your Raspberry Pi is set up for GPIO access and the `RPi.GPIO` library is correctly installed and functioning.
*   The "Switch On" and "Switch Off" actions in the "Discrepancy Finder" sequence will use these relay pin configurations. You'll need to specify the index of the relay (0-7 for an 8-channel module based on the default `RELAY_PINS` list) when setting up these sequence steps.

*(Developer Note: The presence of `core.py` and `camera_model.py` with similar functionalities but different camera libraries (`PiCamera` vs `cv2.VideoCapture`) can be confusing. Consider consolidating these into a single, configurable camera module.)*

## Contributing

Contributions to this project are welcome! If you have ideas for improvements, bug fixes, or new features, please consider the following:

1.  **Fork the repository.**
2.  **Create a new branch for your feature or fix:**
    ```bash
    git checkout -b feature/your-feature-name
    ```
3.  **Make your changes and commit them with clear messages.**
4.  **Push your changes to your fork:**
    ```bash
    git push origin feature/your-feature-name
    ```
5.  **Submit a pull request** to the main repository for review.

Please ensure your code is well-commented and, if applicable, update or add documentation for new features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
