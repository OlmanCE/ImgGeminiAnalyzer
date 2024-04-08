from flask import Flask, request, jsonify
import os
from PIL import Image
import google.generativeai as genai
import tempfile

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limita el tamaño del archivo a 16MB

GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

@app.route('/analyze-image', methods=['POST'])
def analyze_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        # Crear un archivo temporal
        temp_fd, temp_path = tempfile.mkstemp()
        try:
            file.save(temp_path)
            with Image.open(temp_path) as img:
                model = genai.GenerativeModel('gemini-pro-vision')
                response = model.generate_content([img, "Dame una descripción de la imagen"])
                response.resolve()
                description = response.text
            
            # No es necesario llamar a img.close() ya que estamos utilizando el contexto 'with'
            # En caso de error en la generación de la descripción, el archivo temporal se eliminará en el bloque 'except'
            # Eliminar el archivo temporal después de usarlo
            os.close(temp_fd)  # Asegúrate de cerrar el descriptor de archivo antes de intentar eliminar el archivo
            os.remove(temp_path)
            
            return jsonify({'description': description})
        except Exception as e:
            # Intenta eliminar el archivo temporal en caso de error también
            os.close(temp_fd)
            os.remove(temp_path)
            return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
