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
#from BAC_calc import widmark
from pydantic import BaseModel

app = FastAPI()

class BACInput(BaseModel):
    weight: float      
    sex: str
    alc_g: float
    hrs: float

@app.get("/")
def root():
    return {"message": "Hello from FastAPI!"}

@app.post("/bac")
async def calculate_bac(data: BACInput):
    weight = data.weight
    sex = data.sex
    total_g = data.alc_g
    hours = data.hrs

    if sex == "male":
#        bac = widmark(total_g, weight, 0.68 ,hours) 
        pass
    else:
#        bac = widmark(total_g, weight, 0.55 ,hours)
        pass 
    
#    return {"bac": bac}
 
