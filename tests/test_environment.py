def test_core_imports():
    import cv2
    import numpy
    import pandas
    import pycocotools

    import data4cvlab

    assert data4cvlab.__version__ == "0.1.0"
    assert cv2.__version__
    assert numpy.__version__
    assert pandas.__version__
    assert pycocotools
