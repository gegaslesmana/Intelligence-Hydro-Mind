@echo off
echo ========================================
echo   DRAIN-EYE Project Scaffold
echo ========================================

:: ── BACKEND ──
mkdir backend
mkdir backend\app
mkdir backend\app\api
mkdir backend\app\models
mkdir backend\app\services
mkdir backend\app\utils

echo. > backend\app\__init__.py
echo. > backend\app\main.py
echo. > backend\app\api\__init__.py
echo. > backend\app\api\routes_detection.py
echo. > backend\app\api\routes_risk.py
echo. > backend\app\api\routes_dashboard.py
echo. > backend\app\models\__init__.py
echo. > backend\app\models\schemas.py
echo. > backend\app\services\__init__.py
echo. > backend\app\services\yolo_service.py
echo. > backend\app\services\lstm_service.py
echo. > backend\app\services\db_service.py
echo. > backend\app\utils\__init__.py
echo. > backend\app\utils\image_preprocess.py
echo. > backend\requirements.txt

:: ── FRONTEND ──
mkdir frontend
mkdir frontend\src
mkdir frontend\src\components
mkdir frontend\src\pages
mkdir frontend\src\services
mkdir frontend\public

echo. > frontend\src\App.jsx
echo. > frontend\src\main.jsx
echo. > frontend\src\components\Map.jsx
echo. > frontend\src\components\AlertPanel.jsx
echo. > frontend\src\components\RiskChart.jsx
echo. > frontend\src\components\MaintenanceQueue.jsx
echo. > frontend\src\pages\Dashboard.jsx
echo. > frontend\src\pages\UploadPWA.jsx
echo. > frontend\src\pages\History.jsx
echo. > frontend\src\services\api.js
echo. > frontend\index.html

:: ── MODEL ──
mkdir model
mkdir model\yolov8
mkdir model\lstm
mkdir model\datasets
mkdir model\datasets\raw
mkdir model\datasets\labeled
mkdir model\notebooks

echo. > model\yolov8\train.py
echo. > model\yolov8\detect.py
echo. > model\yolov8\data.yaml
echo. > model\lstm\train_lstm.py
echo. > model\lstm\predict_risk.py
echo. > model\notebooks\01_yolo_training.ipynb
echo. > model\notebooks\02_lstm_training.ipynb
echo. > model\notebooks\03_data_exploration.ipynb

:: ── DATA ──
mkdir data
mkdir data\historical_flood
mkdir data\geojson
mkdir data\bmkg
mkdir data\scripts

echo. > data\scripts\fetch_bmkg.py
echo. > data\scripts\process_geojson.py
echo. > data\scripts\load_bpbd.py

:: ── ROOT FILES ──
echo. > .gitignore
echo. > README.md
echo. > docker-compose.yml

echo.
echo ✅ Struktur folder DRAIN-EYE berhasil dibuat!
echo.
echo Folder yang dibuat:
echo   /backend   - FastAPI server
echo   /frontend  - React dashboard + PWA
echo   /model     - YOLOv8 + LSTM training
echo   /data      - Dataset dan scripts
echo.
