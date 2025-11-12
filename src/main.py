"""
MIT License

Copyright (c) 2025 Apostolos Chalis

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

class BACInput(BaseModel):
    weight: float
    sex: str
    alc_g: float
    hrs: float

def widmark(alc_g, weight_kg, ratio, hrs):
    bac = (alc_g / (weight_kg * ratio * 1000)) * 100  # grams alcohol / grams body water * 100
    bac -= 0.015 * hrs
    return max(bac, 0)

@app.get("/")
def root():
    return {"message": "Hello from FastAPI!"}

@app.post("/bac")
async def calculate_bac(data: BACInput):
    ratio = 0.68 if data.sex == "male" else 0.55
    bac = widmark(data.alc_g, data.weight, ratio, data.hrs)
    return {"bac": round(bac, 4)}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
