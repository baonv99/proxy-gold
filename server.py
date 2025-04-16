from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Bật CORS cho toàn bộ ứng dụng

# Endpoint proxy
@app.route('/api/gold-price')
def get_gold_price():
    try:
        # Gọi API BTMC
        api_url = "http://api.btmc.vn/api/BTMCAPI/getpricebtmc?key=9999"
        response = requests.get(api_url)
        response.raise_for_status()  # Kiểm tra lỗi HTTP
        
        # Trả về dữ liệu từ API
        return jsonify(response.json()), response.status_code
    
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Lỗi kết nối API: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Lỗi server: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)