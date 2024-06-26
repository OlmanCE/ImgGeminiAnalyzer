
# API Muestra una descripción de una imagen
Esta API proporciona un servicio que permite analizar imágenes y generar descripciones textuales utilizando el modelo avanzado gemini-pro-vision de Google Generative AI. El Procfile permite que sea desplegado en Heroku o en Railway, entre otras

## Authors

- [@FabricioAA223](https://github.com/FabricioAA223)
- [@Olmance ](https://github.com/OlmanCE)


## API Reference

#### Obtener las categorias

```http
  POST /analyze_imagen
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `imagen` | `jpg` | Imagen de no más de 16 MB|

#### Get item
Devuelve una descripcion de lo que hay en la imagen


Retorna una descripción de lo que hay en la imagen. 
## Deployment 
Para utilizar la API, los clientes deben enviar una solicitud POST al endpoint /analyze-image con una imagen adjunta. La API procesa la imagen y devuelve una descripción textual del contenido visual. La interfaz es simple y fácil de usar, diseñada para una rápida integración en cualquier sistema que requiera capacidades de análisis de imágenes. En el archivo requeriments se encuentran las bibliotecas necesarias. 
## Documentation
Se requiere una cuenta de Google, esto debido a que se debe crear un proyecto en Google Cloud, y Google Studio https://ai.google.dev/docs se adjunta guía para Python https://ai.google.dev/tutorials/python_quickstart  
Por ultimos se debe obtener una Key y ligarla al proyecto creado en Google Cloud https://ai.google.dev/tutorials/setup 
## Screenshots

![Prueba desde Postman](image.png)