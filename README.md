# FAATerminalProcedures

This script downloads pdf charts from the FAA Digital Terminal Procedures Publication.
https://www.faa.gov/air_traffic/flight_info/aeronav/digital_products/dtpp/search/
Call DTPP.py and pass in airport identifiers in the arguments list.
Requires python 3.5+

## Usage

Download charts to the present working directory. <br />
./DTPP.py kjfk katl lax <br />
Downloads chart to other directory evaluation. <br />
./DTPP.py kvrb kfpr -d /somepath

# License

MIT License

Copyright (c) 2016 amavumkal

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
