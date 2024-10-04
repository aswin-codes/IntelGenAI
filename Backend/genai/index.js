const express = require('express');
const { GoogleGenerativeAI } = require('@google/generative-ai');
const axios = require('axios');
const bodyParser = require('body-parser');

const app = express();
const port = 3000;

// Initialize the Generative AI model
const genAI = new GoogleGenerativeAI('AIzaSyBc9DJ0jSt6ojoAciC9OnEp1DQ_apOvGUc');

app.use(bodyParser.json());

app.get("/",(req,res) => {
    return res.send("Ji")
})

app.post('/analyze-image', async (req, res) => {
  const { imageUrl } = req.body;

  if (!imageUrl) {
    return res.status(400).json({ error: 'Image URL is required' });
  }

  try {

    // Fetch the image data
    const response = await axios.get(imageUrl, { responseType: 'arraybuffer' });
    const imageBuffer = Buffer.from(response.data, 'binary');

    // Create a GenerativeModel instance
    const model = genAI.getGenerativeModel({ model: 'gemini-1.5-flash' });

    // Prepare the image parts for the API request
    const imageParts = [
      {
        inlineData: {
          data: imageBuffer.toString('base64'),
          mimeType: response.headers['content-type']
        }
      }
    ];

    // Generate content
    const result = await model.generateContent(['Analyze the disease and possible remedy', ...imageParts]);
    const generatedContent = await result.response;
    const text = generatedContent.text();
    console.log(text)
    res.json({ analysis: text });
  } catch (error) {
    console.error('Error:', error);
    res.status(500).json({ error: 'An error occurred while processing the image.' });
  }
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});