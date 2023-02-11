from analyze_water import calc_turb, min_time
import pytest

turbidity_data = {
  "turbidity_data": [
    {
      "datetime": "2023-02-01 00:00",
      "sample_volume": 1.19,
      "calibration_constant": 1,
      "detector_current": 1,
      "analyzed_by": "C. Milligan"
    },
    {
      "datetime": "2023-02-01 01:00",
      "sample_volume": 1.15,
      "calibration_constant": 2,
      "detector_current": 2,
      "analyzed_by": "C. Milligan"
    },
    {
      "datetime": "2023-02-01 02:00",
      "sample_volume": 1.15,
      "calibration_constant": 3,
      "detector_current": 3,
      "analyzed_by": "C. Milligan"
    },
    {
      "datetime": "2023-02-01 03:00",
      "sample_volume": 1.18,
      "calibration_constant": 4,
      "detector_current": 4,
      "analyzed_by": "R. Zhang"
    },
    {
      "datetime": "2023-02-01 04:00",
      "sample_volume": 1.19,
      "calibration_constant": 5,
      "detector_current": 5,
      "analyzed_by": "J. Maertz"
    }
    ]
}
def test_calc_turb():
    assert calc_turb(turbidity_data) == 11  

def test_min_time():
    assert min_time(11) == 118.69177903294941
