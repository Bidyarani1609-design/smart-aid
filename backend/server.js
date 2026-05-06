// const express = require("express");

// const app = express();

// app.get("/", (req, res) => {
//   res.send("Backend working");
// });

// app.listen(5000, () => {
//   console.log("Server running on port 5000");
// });
// const cors = require("cors");
// app.use(cors());
const express = require("express")
const cors = require("cors")
const multer = require("multer")
const axios = require("axios")
const FormData = require("form-data")
const fs = require("fs")

const app = express()

// File upload config
const upload = multer({ dest: "uploads/" })

app.use(cors())
app.use(express.json())

// Health check
app.get("/", (req, res) => {
  res.json({
    status: "OK",
    message: "Smart Aid backend running",
  })
})

// Main prediction route
app.post("/predict", upload.single("image"), async (req, res) => {
  let tempFilePath = null

  try {
    // Validate image
    if (!req.file) {
      return res.status(400).json({ error: "Image is required" })
    }

    tempFilePath = req.file.path

    const { height, weight } = req.body

    if (!height || !weight) {
      return res
        .status(400)
        .json({ error: "Height and weight are required" })
    }

    // Prepare request for Python API
    const formData = new FormData()
    formData.append("file", fs.createReadStream(tempFilePath))
    formData.append("height", height)
    formData.append("weight", weight)

    // Send to FastAPI
    const aiResponse = await axios.post(
      "http://127.0.0.1:8000/predict",
      formData,
      {
        headers: formData.getHeaders(),
      }
    )

    // Send response back to frontend
    res.json({
      success: true,
      data: aiResponse.data,
    })
  } catch (error) {
    console.error("Prediction failed:", error.message)

    res.status(500).json({
      success: false,
      error: "Failed to process image",
    })
  } finally {
    // Clean temp file
    if (tempFilePath && fs.existsSync(tempFilePath)) {
      fs.unlinkSync(tempFilePath)
    }
  }
})

// Start server
app.listen(5000, () => {
  console.log("Server running on http://localhost:5000")
})