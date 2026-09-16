## with existing venv
solver success=False
solver success=False
  LS    RMSE = 1457.364860292828  [0x1.6c5759defc539p+10]
  **LAD   RMSE = 1470.528582973419  [0x1.6fa1d44dae03ap+10]**
  NNLS  RMSE = 1563.5478871298567  [0x1.86e310952e289p+10]
  **NNLAD RMSE = 1567.8444942493943  [0x1.87f60c319bb3cp+10]**

## with venv reinstalled from uv.lock
solver success=False
solver success=False
  LS    RMSE = 1457.364860292828  [0x1.6c5759defc539p+10]
  **LAD   RMSE = 1470.528582973419  [0x1.6fa1d44dae03ap+10]**
  NNLS  RMSE = 1563.5478871298567  [0x1.86e310952e289p+10]
  **NNLAD RMSE = 1567.8444942493943  [0x1.87f60c319bb3cp+10]**

## with unpinned dependency bump
solver success=True
solver success=True
  LS    RMSE = 1457.364860292828  [0x1.6c5759defc539p+10]
  **LAD   RMSE = 1470.528567077177  [0x1.6fa1d40b018dfp+10]**
  NNLS  RMSE = 1563.5478871298567  [0x1.86e310952e289p+10]
  **NNLAD RMSE = 1567.8443940386974  [0x1.87f60a8d4b492p+10]**